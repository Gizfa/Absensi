import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate(
    "venv/faceattendacerealtime-e6a22-firebase-adminsdk-q0xu6-016ed4fa53.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-e6a22-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "faceattendacerealtime-e6a22.appspot.com"

})

# importing the student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    # print(path)
    # print (os.path.splitext(path)[0])
print(studentIds)

fileName = f'{folderPath}/{path}'
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Starting....")
encodeListKnown = findEncodings(imgList)
encodeListKnownIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownIds, file)
file.close()
print("File Saved")
