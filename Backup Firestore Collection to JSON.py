import json

def backup_collection(collection_name):
    docs = db.collection(collection_name).stream()
    data = {doc.id: doc.to_dict() for doc in docs}
    with open(f"{collection_name}_backup.json", 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Backup of '{collection_name}' completed.")

backup_collection('users')
