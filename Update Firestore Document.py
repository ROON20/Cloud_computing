import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def update_data(collection, document_id, data):
    db.collection(collection).document(document_id).update(data)
    print(f"Document '{document_id}' updated with {data}.")

update_data('users', 'user1', {'email': 'newemail@example.com'})
