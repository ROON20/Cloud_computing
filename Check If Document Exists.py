def document_exists(collection, document_id):
    doc = db.collection(collection).document(document_id).get()
    print(f"Document Exists: {doc.exists}")

document_exists('users', 'user1')
