def list_storage_files(folder):
    blobs = bucket.list_blobs(prefix=folder)
    for blob in blobs:
        print(blob.name)

list_storage_files('uploads/')
