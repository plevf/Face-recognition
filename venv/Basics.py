import cv2
import numpy as np
import face_recognition
#venv - virtual environment

# loading images to compare
imgFrusciante = face_recognition.load_image_file('ImageBasic/frusciante.jpg')
# converting pics from BGR to RGB
imgFrusciante = cv2.cvtColor(imgFrusciante, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImageBasic/fruscianteTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# opens the image in a new window
cv2.imshow('Frusciante', imgFrusciante)
cv2.imshow('Frusciante Test', imgTest)
cv2.waitKey(0) # waits until a key is pressed

# finding the location of the face in the image
faceLoc = face_recognition.face_locations(imgFrusciante)[0]
encodeFrusciante = face_recognition.face_encodings(imgFrusciante)[0]
cv2.rectangle(imgFrusciante, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
# faceLoc returns a list of tuples (top, right, bottom, left)
# cv2.rectangle(image, start_point, end_point, color, thickness)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeFruscianteTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)