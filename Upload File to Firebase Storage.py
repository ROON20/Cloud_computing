from firebase_admin import storage

bucket = storage.bucket()

def upload_file(local_path, cloud_path):
    blob = bucket.blob(cloud_path)
    blob.upload_from_filename(local_path)
    print(f"File '{local_path}' uploaded to '{cloud_path}'.")

upload_file('localfile.txt', 'uploads/localfile.txt')
