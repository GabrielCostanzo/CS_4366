import flask
import pymongo
from pymongo import MongoClient
from flask import request
import datetime


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
        return {"User": self.user, "Listing_ID": self.lid, "Bid_Amount": self.bid_amt, "Time": self.time}

# returns all bids associated with a listing
@app.route('/bid_service/getBids', methods=['GET'])
def getBids():
    if 'lid' in request.args:
        lid = request.args.getlist('lid')
    else:
        return {"Success": False, "Error Message": "Invalid LID"}

    # returns list of bids for lid
    listing = collection.find_one({"_id": lid})
    bid_list = listing["Bids"]
    return bid_list

# updates bid list of a listing if the new bid is higher than the previous
@app.route('/bid_service/placeBid', methods=['GET'])
def placeBid():
    # get user id
    if 'uid' in request.args:
        uid = request.args.getlist('uid')
    else:
        return {"Success": False, "Error Message": "Invalid UID"}

    # get listing id
    if 'lid' in request.args:
        lid = request.args.getlist('lid')
    else:
        return {"Success": False, "Error Message": "Invalid LID"}

    # get bid amount
    if 'bid_amt' in request.args:
        bid_amt = request.args.getlist('bid_amt')
    else:
        return {"Success": False, "Error Message": "Invalid Bid Amount"}

    # creates new bid object
    new_bid = Bid(uid, bid_amt)

    # get bids associated with lid
    listing = collection.find_one({"_id": lid})

    # find highest bid that has been made on the product
    bid_list = listing["Bids"]
    if bid_list is []:
        highest_bid = -1
    else:
        highest_bid = bid_list[-1]

    # update highest bid
    if bid_amt > highest_bid["Bid_Amount"]:
        bid_list.append(new_bid.convertToJSON())
        collection.update_one({"_id": lid}, {"$set", {"Bids": bid_list}})
        # give Nick data of person who was previously out-bid
        r = request.post("http://bugs.python.org/?uid=" + highest_bid.user + "&lid=" + lid)
        return {"Success": True}
    else:
        return {"Success": False, "Error Message": "Invalid Bid"}