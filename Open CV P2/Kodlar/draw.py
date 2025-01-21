import face_recognition
from PIL import Image,ImageDraw


img = face_recognition.load_image_file("C:\\OpenCV_Udemy\\Face_recognation\\images\\face.jpg")

landmarks = face_recognition.face_landmarks(img)

PIL = Image.fromarray(img)
d = ImageDraw.Draw(PIL)


for landmark in landmarks:
    for feature in landmark.keys():
        d.line(landmark[feature],width=1)

PIL.show()