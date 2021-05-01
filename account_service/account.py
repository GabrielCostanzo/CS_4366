from flask import Flask, request, jsonify
import flask
#from passlib.hash import pbkdf2_sha256 
import pymongo
from pymongo import MongoClient
import uuid

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.run()

client = pymongo.MongoClient("mongodb+srv://atharva:atharva@cluster0.jnzyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["user_service"]
collection = db["account"]

class Account():
    def __init__(self, username, password, email, first_name, verified):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.verified = verified

        
    def createAccount(self):
        client = pymongo.MongoClient("mongodb+srv://atharva:atharva@cluster0.jnzyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client["user_service"]
        collection = db["account"]
        data = {"_id": uuid.uuid4(), "username" : self.username, "password" : self.password,
                "email" : self.email, "first_name" : self.first_name, "verified" : verified}
        db.collection.insert_one(data)



class Login():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def login(self):
        client = pymongo.MongoClient("mongodb+srv://atharva:atharva@cluster0.jnzyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client["user_service"]
        collection = db["account"]
        user = collection.find_one({"username" : username})
        if user['password'] == password:
            return True
        else:
            return False

    



