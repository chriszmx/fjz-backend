import firebase_admin
from firebase_admin import credentials
import keyfile


def initialize_firebase():
    cred = credentials.Certificate(keyfile.json)
    firebase_admin.initialize_app(cred)
