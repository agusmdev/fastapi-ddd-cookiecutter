import uuid
from collections import defaultdict

# FIRESTORE
# import firebase_admin
# from firebase_admin import credentials, firestore_async
import simplejson as json


class UUIDEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, uuid.UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(o)
        return self.default(o)


def get_async_firestore_client():
    ...


# def get_async_firestore_client():
#     cred = credentials.Certificate(settings.GOOGLE_CREDENTIALS)
#     firebase_admin.initialize_app(cred)
#     return firestore_async.client()


in_memory_session = defaultdict(dict)
