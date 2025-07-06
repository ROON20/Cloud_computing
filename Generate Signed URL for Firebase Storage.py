import datetime

def generate_signed_url(cloud_path, expiry_minutes=60):
    blob = bucket.blob(cloud_path)
    url = blob.generate_signed_url(datetime.timedelta(minutes=expiry_minutes))
    print("Generated Signed URL:", url)

generate_signed_url('uploads/sample.txt')
