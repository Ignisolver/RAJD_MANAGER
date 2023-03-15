import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import SHEET_ID, SAMPLE_RANGE, STATUS_RANGE, TOKEN_PATH
from persons_manager import Persons
from utils import Person


class MySheet:
    def __init__(self):
        self._creds = None
        self._sheet = None
        self.SHEET_ID = SHEET_ID
        self._authenticate_sheets()
        self._connect_sheet()

    def _connect_sheet(self):
        service = build('sheets', 'v4', credentials=self._creds)
        self._sheet = service.spreadsheets()

    def _authenticate_sheets(self):
        token_path = TOKEN_PATH.joinpath('token.json')
        if os.path.exists(token_path):
            self._creds = Credentials.from_authorized_user_file(token_path,
                                                                [])

    def get_persons(self):
        result = self._sheet.values().get(spreadsheetId=self.SHEET_ID,
                                          range=SAMPLE_RANGE,
                                          majorDimension="ROWS").execute()
        values = result.get('values', [])
        ids = iter(range(1, len(values) + 1))
        persons = [Person(next(ids), *data) for data in values]
        return Persons(persons)

    def update_statuses(self, statuses):
        body = {
            'values': statuses
        }
        self._sheet.values().update(
            spreadsheetId=self.SHEET_ID, range=STATUS_RANGE,
            valueInputOption="RAW", body=body).execute()
