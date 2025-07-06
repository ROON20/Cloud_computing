import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
def query_collection(collection, field, value):
    results = db.collection(collection).where(field, '==', value).stream()
    for doc in results:
        print(f"{doc.id} => {doc.to_dict()}")

query_collection('products', 'name', 'Apple')
