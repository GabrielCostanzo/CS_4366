from flask import Flask, request, jsonify
import flask
import pymongo
from pymongo import MongoClient
import uuid
from account_service.account import Account, Login


app = flask.Flask(__name__)
app.config["DEBUG"] = True


client = pymongo.MongoClient("mongodb+srv://atharva:atharva@cluster0.jnzyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["user_service"]
collection = db["account"]

@app.route('/createUser', methods=['GET'])
def signup():

    if 'email' in request.args:
        email = request.args.getlist('email')[0]
    else:
        return {"Success": False, "Error Message": "Invalid email"}

    if 'username' in request.args:
        username = request.args.getlist('username')[0]
    else:
        return {"Success": False, "Error Message": "Invalid username"}

    if 'password' in request.args:
        password = request.args.getlist('password')[0]
    else:
        return {"Success": False, "Error Message": "Invalid password"}

    if 'first_name' in request.args:
        first_name = request.args.getlist('first_name')[0]
    else:
        return {"Success": False, "Error Message": "Invalid first_name"}

    verified = True
    id = uuid.uuid4().hex


    if not (db.collection.find_one({"email" : email})):
    #new_user = Account(username, password, email, first_name, verified)
        data = {"_id": id, "username" : username, "password" : password,
                        "email" : email, "first_name" : first_name, "verified" : True}

        db.collection.insert_one(data)

        return {
                "Success": True,
                "data":       
                    {             
                        "accountId" : id,
                        "password" : password,
                        "first_name" : first_name,  
                        "verified": verified    
                    }
            }
    else:
        return {
                "Success": False,
                "data" : "Create account failed/user already exists"
                } 



@app.route('/login', methods=['GET'])
def login():
    
    if 'username' in request.args:
        username = request.args.getlist('username')[0]
    else:
        return {"Success": False, "Error Message": "Invalid username"}

    if 'password' in request.args:
        password = request.args.getlist('password')[0]
    else:
        return {"Success": False, "Error Message": "Invalid password"}

    user = db.collection.find_one({"username" : username})
    success = False
    if user and user["password"] == password:
        success = True

    if success:

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
                "Success": False,
                "data" : "Login attempt failed"
                }



@app.route('/getUser', methods=['GET'])
def getUserDetails():

    if 'uid' in request.args:
        uid = request.args.getlist('uid')[0]
    else:
        return {"Success": False, "Error Message": "Invalid uid"}

    user = collection.find_one({"_id" : uid})

    if not user:
        return {"Success": False,
                "Error": "User not found"}
    else:
        return { "Email": user["email"],
                "Name" : user["name"]}

    

@app.errorhandler(400)
def page_not_found(e):
    return '''<h1>400</h1>
    <p>The resource could not be found</p>''', 400



app.run()