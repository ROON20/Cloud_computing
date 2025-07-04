import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

print("Firebase app initialized successfully.")

db = firestore.client()

def upload_data(collection, document_id, data):
    db.collection(collection).document(document_id).set(data)
    print(f"Document '{document_id}' added to collection '{collection}'.")

upload_data('users', 'user1', {'name': 'John Doe', 'email': 'john@example.com'})
