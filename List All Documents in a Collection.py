import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def list_documents(collection):
    docs = db.collection(collection).stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

list_documents('users')
