import flask
import pymongo
from pymongo import MongoClient
from flask import request
from datetime import datetime
import json


cluster = MongoClient("mongodb+srv://nicolas:capstone1@cluster0.vfv8c.mongodb.net/capstone?retryWrites=true&w=majority")

db = cluster["capstone"]
collection = db["collection"]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class Bid():
    def __init__(self, user, bid_amt):
        self.user = user
        self.bid_amt = bid_amt
        self.time = datetime.now()

    def convertToJSON(self):
        return {"User": self.user, "Bid_Amount": self.bid_amt, "Time": self.time}

# returns all bids associated with a listing
@app.route('/bid_service/getBids', methods=['GET'])
def getBids():
    if 'lid' in request.args:
        lid = int(request.args.getlist('lid')[0])
    else:
        return {"Success": False, "Error Message": "Invalid LID"}

    # returns list of bids for lid
    listing = collection.find_one({"_id": lid})
    bid_list = listing["Bids"]
    return {"Success": True, "data": bid_list}

# returns all closing prices for a product
@app.route('/bid_service/getHistoricalPrices', methods=['GET'])
def getHistoricalPrices():
    if 'pid' in request.args:
        pid = request.args.getlist('pid')[0]
        print(pid)
    else:
        return {"Success": False, "Error Message": "Invalid PID"}

    # returns list of bids for lid
    listings = collection.find({"Product.DrinkName": pid, "Status": "Closed"})
    bid_list = []
    for listing in listings:
        bid_list.append(listing["Bids"][-1])
    return {"Success": True, "data": bid_list}

# updates bid list of a listing if the new bid is higher than the previous
@app.route('/bid_service/placeBid', methods=['GET'])
def placeBid():
    # get user id
    if 'uid' in request.args:
        uid = request.args.getlist('uid')[0]
    else:
        return {"Success": False, "Error Message": "Invalid UID"}

    # get listing id
    if 'lid' in request.args:
        lid = int(request.args.getlist('lid')[0])
    else:
        return {"Success": False, "Error Message": "Invalid LID"}

    # get bid amount
    if 'bid_amt' in request.args:
        bid_amt = float(request.args.getlist('bid_amt')[0])
    else:
        return {"Success": False, "Error Message": "Invalid Bid Amount"}

    # creates new bid object
    new_bid = Bid(uid, bid_amt)

    # get bids associated with lid
    listing = collection.find_one({"_id": lid})

    # find highest bid that has been made on the product
    bid_list = listing["Bids"]
    if bid_list == []:
        bid_list.append(new_bid.convertToJSON())
        print("=========================================================")
        print(bid_list)
        db.collection.update_one({'_id':lid},
                                {'$set': {"Bids": bid_list}}, 
                                upsert=True)

        return {"Success": True}
    else:
        highest_bid = bid_list[-1]

    # update highest bid
    if bid_amt > highest_bid["Bid_Amount"]:
        bid_list.append(new_bid.convertToJSON())
        db.collection.update_one({'_id':lid},
                                {'$set': {"Bids": bid_list}}, 
                                upsert=True)
        # give Nick data of person who was previously out-bid
        #r = request.post("http://bugs.python.org/?uid=" + highest_bid.user + "&lid=" + lid)
        return {"Success": True}
    else:
        return {"Success": False, "Error Message": "Invalid Bid"}

app.run(host='0.0.0.0', port=23450)