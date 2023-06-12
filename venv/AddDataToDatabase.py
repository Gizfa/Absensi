import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("venv/faceattendacerealtime-e6a22-firebase-adminsdk-q0xu6-016ed4fa53.json")
firebase_admin.initialize_app(cred,{
'databaseURL':"https://faceattendacerealtime-e6a22-default-rtdb.asia-southeast1.firebasedatabase.app/"

})

ref = db.reference('Students')

data = {
"423154":
    {
        "name": "Gizfa Satria Putra Pamungkas",
        "major": "ELIND",
        "strating_year":"2020",
        "total_attendance": "6",
        "standing": "G",
        "years": "4",
        "last_attendance_time" : "2022-12-11 00:55:34"
    },
"2003428":
    {
        "name": "Rifki Bur Zain",
        "major": "ELIND",
        "strating_year":"2020",
        "total_attendance": "6",
        "standing": "G",
        "years": "4",
        "last_attendance_time" : "2022-12-11 00:55:34"
    }


}
    

for key,value in data.items():
    ref.child(key).set(value)