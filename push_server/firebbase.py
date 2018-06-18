import firebase_admin
from firebase_admin import credentials, auth



cred = credentials.Certificate('./tacotron-20180417-firebase-adminsdk-yt4k7-4a411a75e4.json')
default_app = firebase_admin.initialize_app(cred)
