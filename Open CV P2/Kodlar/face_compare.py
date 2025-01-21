import face_recognition
import cv2

img = cv2.imread("C:\\OpenCV_Udemy\\Face_recognation\\images\\test.jpg")


train_face = face_recognition.load_image_file("C:\\OpenCV_Udemy\\Face_recognation\\images\\train.jpg")
train_face_encode = face_recognition.face_encodings(train_face)


test_face = face_recognition.load_image_file("C:\\OpenCV_Udemy\\Face_recognation\\images\\test.jpg")
test_face_loc = face_recognition.face_locations(test_face)
test_face_encode = face_recognition.face_encodings(test_face,test_face_loc)[0]

mathed_faces = face_recognition.compare_faces(train_face_encode,test_face_encode)

print(test_face_loc)

if True in mathed_faces:
    cv2.rectangle(img, (812,99), (1133,420), (0, 255, 0), 2)
    cv2.putText(img, "Keaune Reves", (812,99), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

    cv2.imshow("pencere", img)
    cv2.waitKey(0)



"""elif mathed_faces == False:
    #cv2.rectangle(img,(test_face_loc[0],test_face_loc[3]),(test_face_loc[1],test_face_loc[2]),(0,255,0),2)
    #cv2.putText(img,"Unknown",(test_face_loc[0],test_face_loc[3]),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
    cv2.imshow("pencere",img)
    cv2.waitKey(0)
"""