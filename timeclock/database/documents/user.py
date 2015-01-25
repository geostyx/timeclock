import mongoengine as db
import json


# Class for standard users
class User(db.Document):
    username = db.StringField(required=True, min_length=3, max_length=32)
    upper_username = str(username).upper()  # To make quarries easier
    first_name = db.StringField(required=False, max_length=32)
    last_name = db.StringField(required=False, max_length=32)
    email = db.StringField(required=False, max_length=50)
    password = db.StringField(required=False, max_length=256)