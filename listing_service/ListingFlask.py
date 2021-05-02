import flask
import pymongo
from pymongo import MongoClient
import flask
from flask import request
from Listing import Listing



client = pymongo.MongoClient("mongodb+srv://nicolas:capstone1@cluster0.vfv8c.mongodb.net/capstone?retryWrites=true&w=majority")
db = client["capstone"]
ListingCollection = db["collection"]
ProductCollection = db["ProductCollection"]
db.ProductCollection.create_index([('DrinkName', pymongo.ASCENDING)], unique=True)

product1 = {"_id": 1,
            "DrinkName": "Black Bowmore 1964",
            "DrinkBrand": "Black Bowmore",
            "AlcoholType": "Scotch Whiskey",
            "AlcoholPercentage": "40",
            "Volume": "700ml",
            "CountryOfOrigin": "Scotland",
            "Description": "The 1964 expression is fruity and almost rum-like, but remarkably not over-oaked even after spending half a century in wood."}
product2 = {"_id": 2,
            "DrinkName": "Paradis Imperial",
            "DrinkBrand": "Hennessy",
            "AlcoholType": "Whiskey",
            "AlcoholPercentage": "40",
            "Volume": "750ml",
            "CountryOfOrigin": "France",
            "Description": "This is a very special cognac with deep, fruity notes that call to mind a rum or aged whiskey."}
product3 = {"_id": 3,
            "DrinkName": "The Boss Hog - The Black Prince ",
            "DrinkBrand": "WhistlePig",
            "AlcoholType": "Whiskey",
            "AlcoholPercentage": "59",
            "Volume": "750ml",
            "CountryOfOrigin": "Vermont",
            "Description": "the first rye to be finished in armagnac casks, giving it notes of apricot and warm apple crisp. This limited release bottling consists of 14-year-old sourced whiskey with a mash bill of 95 percent rye that was bottled at cask strength."}
product4 = {"_id": 4,
            "DrinkName": "XO",
            "DrinkBrand": "Hennessey",
            "AlcoholType": "Cognac",
            "AlcoholPercentage": "72",
            "Volume": "1500", "CountryOfOrigin": "France",
            "Description": "X.O. is a blend of 100 eaux-de-vie that ranges in age from six to 30 years old. The liquid inside is excellent, warm, and a little bit spicy."}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getNumberOfListings', methods=['GET'])
def findDrink():
    num = int(request.args['num'])
    results = ListingCollection.find()
    list_results = list(results)
    colLength = ListingCollection.count_documents({})
    if num > colLength:
        return {"Success": False,"count": colLength, "Error": "Error the number of requests is greater than the amount of products in the database"}
    else:
        return {"Success": True, "data": list_results[:num]}

@app.route('/getOpenListing', methods=['GET'])
def getListing():
        results = ListingCollection.find({"Status": "Open"})
        list_results = list(results)
        colLength = ListingCollection.count_documents({})
        # conditional for 400 error
        if colLength == 0:
            return {"Success": False,
                    "Error": "400"}
        return {"Success": True, "data": list_results}

@app.route('/getListingbyID', methods=['GET'])
def getListingbyID():
        reqId = int(request.args['reqId'])
        results = ListingCollection.find({"_id": reqId})
        list_results = list(results)
        colLength = ListingCollection.count_documents({})
        if colLength == 0:
            return {"Success": False,
                    "Error": "400"}
        else:
            return {"Success": True,
                    "data": list_results}

@app.route('/MakeListing', methods=['GET'])
def MakeListing():

    type = str(request.args['type'])
    terminatingprice = float(request.args['termprice'])
    status = str(request.args['status'])
    startingprice = float(request.args['startingprice'])
    seller = str(request.args['seller'])
    expirationdate = str(request.args['expirationdate'])

    productid = int(request.args['id'])
    drinkname = str(request.args['drinkname'])
    drinkbrand = str(request.args['drinkbrand'])
    volume = str(request.args['volume'])
    alcoholtype = str(request.args['alcoholtype'])
    alcoholpercentage = str(request.args['alcoholpercentage'])
    countryoforigin = str(request.args['countryoforigin'])
    image = request.files['image']
    description = str(request.args['description'])



    product = {
        "_id": productid,
        "DrinkName": drinkname,
        "DrinkBrand": drinkbrand,
        "AlcoholType": alcoholtype,
        "AlcoholPercentage": alcoholpercentage,
        "Volume": volume,
        "CountryOfOrigin": countryoforigin,
        "Description": description
    }
    #checkifexist = db.ProductCollection.find()
    #if drinkname != checkifexist:
    db.ProductCollection.insert_one(product)
    listing = Listing(type, terminatingprice, drinkname, seller, startingprice, expirationdate, status)
    listing.insertMongodb()


@app.errorhandler(400)
def page_not_found(e):
    return '''<h1>400</h1>
    <p>The resource could not be found</p>''', 400

<<<<<<< HEAD
Listing1 = Listing("Bid", 12.00, "XO", "Redbear", 25.00, "12/12/2022", "Open")
Listing2 = Listing("Bid", 18.00, "Paradis Imperial", "gressy", 25.00, "02/04/2023", "Open")
Listing3 = Listing("Bid", 17.00, "Black Bowmore 1964", "jordan", 26.00, "04/05/2023", "Closed")
Listing4 = Listing("Bid", 12.00, "XO", "Redbear", 25.00, "12/12/2022", "Open")
Listing5 = Listing("Bid", 18.00, "Paradis Imperial", "gressy", 25.00, "02/04/2023", "Open")
Listing6 = Listing("Bid", 17.00, "Black Bowmore 1964", "jordan", 26.00, "04/05/2023", "Closed")
Listing7 = Listing("Bid", 12.00, "XO", "Redbear", 25.00, "12/12/2022", "Open")
Listing8 = Listing("Bid", 18.00, "Paradis Imperial", "gressy", 25.00, "02/04/2023", "Open")
Listing9 = Listing("Bid", 17.00, "Black Bowmore 1964", "jordan", 26.00, "04/05/2023", "Closed")

#Listing1.insertMongodb()
#Listing2.insertMongodb()
#Listing3.insertMongodb()
#Listing4.insertMongodb()
#Listing5.insertMongodb()
#Listing6.insertMongodb()
#Listing7.insertMongodb()
#Listing8.insertMongodb()
#Listing9.insertMongodb()

=======
#Listing1 = Listing("Bid", 12.00, "XO", "Redbear", 25.00, "12/12/2022", "Open")
#Listing2 = Listing("Bid", 15.00, "The Boss Hog - The Black Prince", "Idontknow", 30.00, "05/04/2022", "Open")
#Listing3 = Listing("Bid", 18.00, "Paradis Imperial", "gressy", 25.00, "02/04/2023", "Open")
#Listing4 = Listing("Bid", 19.00, "Black 1964", "jordan", 26.00, "04/05/2023", "Closed")
>>>>>>> a6456b2545b84a8311531464ef5c971d2d8e9b55

app.run()
#db.ProductCollection.insert_one(product1)
#db.ProductCollection.insert_one(product2)
#db.ProductCollection.insert_one(product3)
#db.ProductCollection.insert_one(product4)
#Listing1.insertMongodb()
#Listing2.insertMongodb()
#Listing3.insertMongodb()
