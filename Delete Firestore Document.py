import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def delete_document(collection, document_id):
    db.collection(collection).document(document_id).delete()
    print(f"Document '{document_id}' deleted from collection '{collection}'.")

delete_document('users', 'user1')
