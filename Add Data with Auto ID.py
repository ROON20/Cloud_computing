import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_data_auto_id(collection, data):
    ref = db.collection(collection).add(data)
    print(f"Document added with auto-generated ID: {ref[1].id}")

add_data_auto_id('logs', {'event': 'login', 'status': 'success'})
