from flask import Flask, request, jsonify
import flask
#from passlib.hash import pbkdf2_sha256 
import pymongo
from pymongo import MongoClient
import uuid
from account_service.account import Account, Login


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.run()

client = pymongo.MongoClient("mongodb+srv://atharva:atharva@cluster0.jnzyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["user_service"]
collection = db["account"]

@app.route('/createUser', methods=['GET'])
def signup():
    username = "atharva1234"
    password = "atharva1"
    email = "atharvaraibagi@gmail.com"
    first_name = "atharva"
    verified = True
    new_user = Account(username, password, email, first_name, verified)
    Account.createAccount(new_user);


@app.route('/login', methods=['GET'])
def login():
    username = "atharva1234"
    password = "atharva1"
    user = Login(username, password)

    if user.login():

        return {
                "Success": True,
                "data":       
                        {             
                        "accountId" : user["_id"],
                        "password" : user["password"],
                        "first_name" : user["first_name"],  
                        "verified": user["verified"]    
                        }
                }
    else:
        return {
                "Success": True,
                "data" : "Login attempt failed"
                }



@app.route('/getUser', methods=['GET'])
def getUserDetails():
    userId = int(request.args['userId'])
    user = collection.find_one({"_id" : userId})
    if not user:
        return {"Success": False,
                "Error": "400"}
    else:
        return { "Email": user['email'],
                 "Name" : user['name']}


@app.errorhandler(400)
def page_not_found(e):
    return '''<h1>400</h1>
    <p>The resource could not be found</p>''', 400