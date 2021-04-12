from os import getenv

from dotenv import load_dotenv
import pyrebase


load_dotenv()

firebase_config = {
    "apiKey": getenv("FIREBASE_API_KEY"),
    "authDomain": getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": getenv("FIREBASE_APP_ID"),
    "measurementId": getenv("FIREBASE_MEASUREMENT_ID"),
    "databaseURL": getenv("FIREBASE_DATABASE_URL"),
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
