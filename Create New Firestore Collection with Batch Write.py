import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
def batch_insert(collection_name, data_list):
    batch = db.batch()
    for data in data_list:
        ref = db.collection(collection_name).document()
        batch.set(ref, data)
    batch.commit()
    print(f"{len(data_list)} documents inserted into '{collection_name}'.")

batch_insert('products', [{'name': 'Apple'}, {'name': 'Banana'}])
