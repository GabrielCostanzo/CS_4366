import pymongo
import request
from pymongo import MongoClient
import random
class Listing:

    def __init__(self, Type, TerminatingPrice, ProductName, SellerID, StartingPrice, Expiration, Status):
        self.Type = Type
        self.TerminatingPrice = TerminatingPrice
        self.Transaction = None
        self.Product = None
        self.ProductName = ProductName
        self.Seller = None
        self.SellerID = SellerID
        self.StartingPrice = StartingPrice
        self.Expiration = Expiration
        self.Status = Status
        self.getProduct(ProductName)


    def getProduct(self,ProductName):
        cluster = pymongo.MongoClient("mongodb+srv://nicolas:capstone1@cluster0.vfv8c.mongodb.net/capstone?retryWrites=true&w=majority")
        db = cluster["capstone"]
        collection = db["ProductCollection"]
        result = collection.find_one({'DrinkName': ProductName})
        self.Product = result

    def insertMongodb(self):
        cluster = pymongo.MongoClient("mongodb+srv://nicolas:capstone1@cluster0.vfv8c.mongodb.net/capstone?retryWrites=true&w=majority")
        db = cluster["capstone"]
        collection = db["Listing"]
        document = {"_id": random.randint(1,10000000), "Type": self.Type, "TerminatingPrice": self.TerminatingPrice, "Transcation": self.Transaction,
                    "Product": self.Product, "Seller": self.SellerID, "StartPrice": self.StartingPrice, "Expiration": self.Expiration, "Status": self.Status}
        db.collection.insert_one(document)