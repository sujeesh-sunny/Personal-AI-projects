import cv2
from deepface import DeepFace

# Load the reference image for face recognition
reference_img_path = 'reference.jpg'
reference_img = cv2.imread(reference_img_path)

# Initialize the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a named window
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Recognition", 640, 480)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if ret:
        # Perform face recognition
        try:
            result = DeepFace.verify(frame, reference_img.copy(), enforce_detection=False)

            if result['verified']:
                cv2.putText(frame, "MATCH", (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "NO MATCH", (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

        except Exception as e:
            print("Error:", str(e))

        # Display the frame
        cv2.imshow("Face Recognition", frame)

    # Check for 'q' key to exit the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

