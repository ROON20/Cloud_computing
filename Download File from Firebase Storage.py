import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
def download_file(cloud_path, local_path):
    blob = bucket.blob(cloud_path)
    blob.download_to_filename(local_path)
    print(f"File '{cloud_path}' downloaded to '{local_path}'.")

download_file('uploads/localfile.txt', 'downloaded.txt')
