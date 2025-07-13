def restore_collection(collection_name, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    for doc_id, doc_data in data.items():
        db.collection(collection_name).document(doc_id).set(doc_data)
    print(f"Data restored to collection '{collection_name}' from '{file_path}'.")

restore_collection('users', 'users_backup.json')
