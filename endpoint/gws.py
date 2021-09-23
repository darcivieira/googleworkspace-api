from time import sleep
from .workspace.connector import GoogleConnector
from rest_framework.views import status
from rest_framework.response import Response


class GoogleWorkspace(GoogleConnector):
    def __init__(
            self,
            scopes: list = None,
            token_file: str = None,
            credential_file: str = None,
            customer_id: str = None
    ):
        super().__init__(scopes, token_file, credential_file)
        self._customer_id = customer_id

    """ Domain """

    def get_all_domains(self) -> dict:
        try:
            domains_obj = self._connection().domains().list(customer=self._customer_id).execute()
        except Exception as error:
            return {'exception_error': error}
        return domains_obj

    """ Users management """

    def get_all_users(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the domains variable is empty
        if not options.get('domain'):
            domains = self.get_all_domains()
            if not domains.get('domains'):
                return Response({"error_message": "The domain option is not a list!"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                options['domain'] = [x.get('domainName') for x in domains['domains']]
                if not isinstance(options['domain'], list):
                    return Response({"error_message": "The domain option is not a list!"},
                                status=status.HTTP_400_BAD_REQUEST)

        if isinstance(options['domain'], str):
            try:
                user_data = self._connection().users().list(orderBy=options.get('orderBy'),
                                                            domain=options.get('domain'),
                                                            projection=options.get('projection'),
                                                            query=options.get('query'),
                                                            event=options.get('event'),
                                                            showDeleted=options.get('showDeleted'),
                                                            pageToken=options.get('pageToken'),
                                                            sortOrder=options.get('sortOrder'),
                                                            maxResults=options.get('maxResults'),
                                                            customer=options.get('customer'),
                                                            customFieldMask=options.get('customFieldMask'),
                                                            viewType=options.get('viewType')
                                                            ).execute()
            except Exception as error:
                return Response({'exception_error': error},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(user_data, status.HTTP_200_OK)

        elif isinstance(options['domain'], list):
            user_list = []
            error_list = []
            for domain in options['domain']:
                if not domain:
                    continue
                while True:
                    try:
                        data_user = self._connection().users().list(orderBy=options.get('orderBy'),
                                                                    domain=domain,
                                                                    projection=options.get('projection'),
                                                                    query=options.get('query'),
                                                                    event=options.get('event'),
                                                                    showDeleted=options.get('showDeleted'),
                                                                    pageToken=options.get('pageToken'),
                                                                    sortOrder=options.get('sortOrder'),
                                                                    maxResults=options.get('maxResults'),
                                                                    customer=options.get('customer'),
                                                                    customFieldMask=options.get('customFieldMask'),
                                                                    viewType=options.get('viewType')
                                                                    ).execute()
                    except Exception as error:
                        error_list.append(error)
                    else:
                        if data_user.get('users'):
                            for user in data_user['users']:
                                user_list.append(user)
                        if data_user.get('nextPageToken'):
                            options['pageToken'] = data_user.get('nextPageToken')
                        else:
                            options['pageToken'] = None
                            break
            if user_list and error_list:
                return Response({"api_response": {"success_message": user_list, "error_message": error_list}},
                                status=status.HTTP_206_PARTIAL_CONTENT)
            elif user_list:
                return Response({"api_response": {"success_message": user_list}},
                                status=status.HTTP_200_OK)
            elif error_list:
                return Response({"api_response": {"error_message": error_list}},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"api_response": {"error_message": "Something went wrong! We could not process your request!"}},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error_message": "You must set domain as a list or a string with your domain name!"},
                            status=status.HTTP_400_BAD_REQUEST)

    def get_user(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the domains variable is empty
        if not options.get('userKey'):
            return Response({"error_message": "The userKey arg must be informed!"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user_data = self._connection().users().get(userKey=options.get('userKey'),
                                                       projection=options.get('projection'),
                                                       customFieldMask=options.get('customFieldMask'),
                                                       viewType=options.get('viewType')
                                                       ).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"api_response": user_data}, status=status.HTTP_200_OK)

    def insert_user(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the domains variable is empty
        if not options.get('primaryEmail') or \
                not options.get('name') or \
                not options.get('password'):
            return Response({"error_message": "You must to fill all required keys!"},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            self._connection().users().insert(body=options).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success_message': 'Account create with success!'},
                        status=status.HTTP_200_OK)

    def update_user(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the domains variable is empty
        if not options.get('body') or not options.get('userKey'):
            return Response({"error_message": "You must to fill all required keys (userKey and body)!"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().users().update(userKey=options.get('userKey'), body=options.get('body')).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success_message': 'Account updated with success!'},
                        status=status.HTTP_200_OK)

    def delete_user(self, options):
        # Looking for a way to transfer all drive data and calendar appointment before delete an account

        # Check the options variable
        if not options or not isinstance(options, dict) or not options.get('userKey'):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().users().delete(userKey=options['userKey']).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success_message': 'Account deleted with success!'},
                        status=status.HTTP_200_OK)

    """ Mobile """

    def get_all_devices(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        if not options.get('pageToken') or options.get('pageToken') != 'all':
            try:
                data_devices = self._connection().mobiledevices().list(customerId=options.get('customerId'),
                                                                       orderBy=options.get('orderBy'),
                                                                       projection=options.get('projection'),
                                                                       pageToken=options.get('pageToken'),
                                                                       maxResults=options.get('maxResults'),
                                                                       sortOrder=options.get('sortOrder'),
                                                                       query=options.get('query')
                                                                       ).execute()
            except Exception as error:
                Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"api_response": data_devices}, status=status.HTTP_200_OK)
        else:
            all_devices = []
            options['pageToken'] = None
            while True:
                print("OI")
                try:
                    data_devices = self._connection().mobiledevices().list(customerId=options.get('customerId'),
                                                                           orderBy=options.get('orderBy'),
                                                                           projection=options.get('projection'),
                                                                           pageToken=options.get('pageToken'),
                                                                           maxResults=options.get('maxResults'),
                                                                           sortOrder=options.get('sortOrder'),
                                                                           query=options.get('query')
                                                                           ).execute()
                except Exception as error:
                    Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    for device in data_devices['mobiledevices']:
                        all_devices.append(device)
                    if data_devices.get('nextPageToken'):
                        options['pageToken'] = data_devices['nextPageToken']
                    else:
                        break
            return Response({"api_response": all_devices}, status=status.HTTP_200_OK)

    def get_all_user_devices(self, options: dict = None):
        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check the email attribute
        if not options.get('email'):
            return Response({"error_message": "You must inform an email"},
                            status=status.HTTP_400_BAD_REQUEST)

        list_user_devices = list(filter(lambda x: options['email'] in x['email'], self.get_all_devices(options)))

        return Response({"api_response": list_user_devices},
                        status=status.HTTP_200_OK)

    def delete_all_user_devices(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check the email attribute
        if not options.get('email'):
            return Response({"error_message": "You must inform an email"},
                            status=status.HTTP_400_BAD_REQUEST)

        user_devices = filter(lambda x: options['email'] in x['email'], self.get_all_devices(options))
        exception_list = []
        index = 0

        for device in user_devices:
            if device.get('type') in ['IOS_SYNC', 'ANDROID'] and device.get('resourceId'):
                try:
                    self._connection().mobiledevices().delete(customerId=options.get('customerId'),
                                                              resourceId=device['resourceId']).execute()
                except Exception as error:
                    exception_list.append([device, error])
                else:
                    index += 1

        if exception_list:
            return Response({"error_message": "We could not remove all devices!", "devices": exception_list},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"success_message": "All user devices were deleted with success!"},
                        status=status.HTTP_200_OK)

    def delete_one_user_device(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check the resourceId attribute
        if not options.get('resourceId'):
            return Response({"error_message": "You must inform the resourceId"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().mobiledevices().delete(customerId=options.get('customerId'),
                                                      resourceId=options['resourceId']).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": "Device deleted with success!"}, status=status.HTTP_200_OK)

    """ Groups """

    def get_all_groups(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        if not options.get('domain') or isinstance(options.get('domain'), str):
            try:
                all_data = self._connection().groups().list(customer=self._customer_id,
                                                            orderBy=options.get('orderBy'),
                                                            domain=options.get('domain'),
                                                            pageToken=options.get('pageToken'),
                                                            maxResults=options.get('maxResults'),
                                                            sortOrder=options.get('sortOrder'),
                                                            query=options.get('query'),
                                                            userKey=options.get('userKey')
                                                            ).execute()
            except Exception as error:
                Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"api_response": all_data}, status=status.HTTP_200_OK)
        elif isinstance(options.get('domain'), list):
            group_list = []
            error_list = []
            for domain in options['domain']:
                options['domain'] = domain
                while True:
                    try:
                        all_data = self._connection().groups().list(customer=self._customer_id,
                                                                    orderBy=options.get('orderBy'),
                                                                    domain=options.get('domain'),
                                                                    pageToken=options.get('pageToken'),
                                                                    maxResults=options.get('maxResults'),
                                                                    sortOrder=options.get('sortOrder'),
                                                                    query=options.get('query'),
                                                                    userKey=options.get('userKey')
                                                                    ).execute()
                    except Exception as error:
                        error_list.append(error)
                    else:
                        if all_data.get('groups'):
                            for group in all_data['groups']:
                                group_list.append(group)
                        if all_data.get('nextPageToken'):
                            options['pageToken'] = all_data.get('nextPageToken')
                        else:
                            break
            if group_list and error_list:
                return Response({"api_response": {"success_message": group_list, "error_message": error_list}},
                                status=status.HTTP_206_PARTIAL_CONTENT)
            elif group_list:
                return Response({"api_response": {"success_message": group_list}},
                                status=status.HTTP_200_OK)
            elif error_list:
                return Response({"api_response": {"error_message": error_list}},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"api_response": {"error_message": "We not found the resquested data!"}},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"api_response": {
                "error_message": "You must set domain as a list or a string with your domain name!"}},
                            status=status.HTTP_400_BAD_REQUEST)

    def get_group(self, options: dict = None):

        # Check the groupkey variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the string groupkey"},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            group = self._connection().groups().get(groupKey=options['groupKey']).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"api_response": group}, status=status.HTTP_200_OK)

    def insert_group(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        if not options.get('email') or not options.get('name'):
            return Response({"error_message": "You must specify both key (email and name)!"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().groups().insert(body=options).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success_message": "Group create with success!"}, status=status.HTTP_200_OK)

    def update_group(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the domains variable is empty
        if not options.get('body') or not options.get('groupKey'):
            return Response({"error_message": "You must to fill all required keys (groupKey and body)!"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().groups().update(groupKey=options.get('groupKey'), body=options.get('body')).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success_message": "Group updated with success!"}, status=status.HTTP_200_OK)

    def delete_group(self, options: dict = None):

        # Check the groupkey variable
        if not options or not isinstance(options, dict) or not options.get('groupKey'):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self._connection().groups().delete(groupKey=options['groupKey']).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success_message": "Group deleted with success!"}, status=status.HTTP_200_OK)

    """ Data Transfer """

    def transfer_all_data(self, options: dict = None):

        # Check the options variable
        if not options or not isinstance(options, dict):
            return Response({"error_message": "You must set the dictionary options"},
                            status=status.HTTP_400_BAD_REQUEST)

        # if not options.get('newOwnerUserId') or not options.get('oldOwnerUserId') or not options.get('body'):
        #     return Response({"error_message": "You must to fill all required keys!"},
        #                     status=status.HTTP_400_BAD_REQUEST)

        try:
            started_transfer = self._admin_transfer().transfers().insert(body=options).execute()
        except Exception as error:
            return Response({'exception_error': error}, status=status.HTTP_400_BAD_REQUEST)
        else:
            while True:
                try:
                    completed_transfer = self._admin_transfer().get(dataTransferId=started_transfer['id']).execute()
                except Exception as error:
                    pass
                else:
                    if completed_transfer['overallTransferStatusCode'] == "completed":
                        return Response({"success_message": "All data has been transferred!"},
                                        status=status.HTTP_200_OK)
                    sleep(10)

