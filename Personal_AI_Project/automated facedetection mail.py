import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import sys

# Load the pre-trained Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Email configuration
sender_email = 'sujeeshsunnyssk1@gmail.com'
receiver_email = 'sujeeshsunnyssk2@gmail.com'
password = 'gmjjnlvkuojgxjnc'  # Use an App Password if 2-step verification is enabled

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_email

flag = False


def send_email_with_image(image_filename):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Face Recognition'

    with open(image_filename, 'rb') as img_file:
        msg.attach(MIMEImage(img_file.read()))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully')
        flag = True  # Set flag to True after sending email
    except Exception as e:
        print('Error sending email:', str(e))
    finally:
        server.quit()

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    if not flag and len(faces) > 0:  # Check flag before sending email
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            face = frame[y:y + h, x:x + w]
            cv2.imwrite('face.jpg', face)
            send_email_with_image('face.jpg')
            flag = True  # Set flag to True after sending email

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()