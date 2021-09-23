import os
from pathlib import Path
from endpoint.gws import GoogleWorkspace


class Workspace:
    @staticmethod
    def __con():
        BASE_DIR = Path(__file__).parent.parent
        scopes = os.getenv('GOOGLE_SCOPES').split('\n')
        token_file = os.path.join(BASE_DIR, os.getenv('GOOGLE_TOKEN_FILE'))
        credential_file = os.path.join(BASE_DIR, os.getenv('GOOGLE_CREDENTIAL_FILE'))
        customer_id = str(os.getenv('GOOGLE_CUSTOMER_ID'))
        return GoogleWorkspace(scopes, token_file, credential_file, customer_id)

    """ USERS """

    def get_user(self, options):
        if not options.get('userKey'):
            return self.__con().get_all_users(options)
        return self.__con().get_user(options)

    def insert_user(self, options):
        return self.__con().insert_user(options)

    def update_user(self, options):
        return self.__con().update_user(options)

    def delete_user(self, options):
        return self.__con().delete_user(options)

    """ GROUPS """

    def get_group(self, options):
        if not options.get('groupKey'):
            return self.__con().get_all_groups(options)
        return self.__con().get_group(options)

    def insert_group(self, options):
        return self.__con().insert_group(options)

    def update_group(self, options):
        return self.__con().update_group(options)

    def delete_group(self, options):
        return self.__con().delete_group(options)

