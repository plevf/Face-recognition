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