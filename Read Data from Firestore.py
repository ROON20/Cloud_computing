import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
print("Firebase app initialized successfully.")

db = firestore.client()


def read_data(collection, document_id):
    doc = db.collection(collection).document(document_id).get()
    if doc.exists:
        print("Document data:", doc.to_dict())
    else:
        print("No such document found.")

read_data('users', 'user1')
