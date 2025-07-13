import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
def increment_field(collection, document_id, field, amount):
    db.collection(collection).document(document_id).update({
        field: firestore.Increment(amount)
    })
    print(f"Field '{field}' incremented by {amount} in document '{document_id}'.")

increment_field('users', 'user1', 'login_count', 1)
