import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

def delete_file(cloud_path):
    blob = bucket.blob(cloud_path)
    blob.delete()
    print(f"File '{cloud_path}' deleted from storage.")

delete_file('uploads/localfile.txt')
