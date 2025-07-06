from firebase_admin import messaging

def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )
    response = messaging.send(message)
    print("Notification sent. Response:", response)

send_push_notification('device_token_here', 'Hello', 'This is a test notification.')
