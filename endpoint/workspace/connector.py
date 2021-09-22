from __future__ import print_function
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleConnector:
    def __init__(
            self,
            scopes: list = None,
            token_file: str = None,
            credential_file: str = None
    ):
        print()
        if not scopes or not token_file or not credential_file:
            raise ValueError('You must define scopes, token file and/or credential file in .env')
        elif not isinstance(scopes, list):
            raise ValueError('The scope must be a list')

        self.__SCOPES = scopes
        self.__token_file = token_file
        self.__credential_file = credential_file

    def _connection(self):
        creds = None
        if os.path.exists(self.__token_file):
            creds = Credentials.from_authorized_user_file(self.__token_file, self.__SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.__credential_file, self.__SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.__token_file, 'w') as token:
                token.write(creds.to_json())
        return build('admin', 'directory_v1', credentials=creds)

    def _admin_transfer(self):
        creds = None
        if os.path.exists(self.__token_file):
            creds = Credentials.from_authorized_user_file(self.__token_file, self.__SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.__token_file, 'w') as token:
                token.write(creds.to_json())
        return build('admin', 'datatransfer_v1', credentials=creds)