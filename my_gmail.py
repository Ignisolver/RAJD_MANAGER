import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import TOKEN_PATH


class MyGmail:
    def __init__(self):
        self._creds = None
        self._service = None
        self._authenticate_gmail()

    def _authenticate_gmail(self):
        token_path = TOKEN_PATH.joinpath('token.json')
        if os.path.exists(token_path):
            self._creds = Credentials.from_authorized_user_file(token_path, [])
        self._service = build('gmail', 'v1', credentials=self._creds)

    def send_message(self, message):
        self._service.users().messages().send(userId="me",
                                              body=message).execute()
