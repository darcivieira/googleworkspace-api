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

    def get_user(self, options):
        if not options.get('userKey'):
            return self.__con().get_all_users(options)
        return self.__con().get_user(options)
