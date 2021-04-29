from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render
import requests
import pprint

class bid():
	def __init__(self, json_bid):
		self.user = json_bid["User"]
		self.bid_amount = json_bid["Bid_Amount"]
		self.time = json_bid["Time"]

class bids():
	def __init__(self, json_bid_list):
		self.bid_list = []
		self.populate_bids(json_bid_list)

	def populate_bids(self, json_bid_list):
		for json_bid in json_bid_list:
			self.bid_list.append(bid(json_bid))

class product():
	def __init__(self, json_product):
		self.alcohol_percentage = json_product["AlcoholPercentage"]
		self.alcohol_type = json_product["AlcoholType"]
		self.country_of_orgin = json_product["CountryOfOrigin"]
		self.description = json_product["Description"]
		self.drink_brand = json_product["DrinkBrand"]
		self.drink_name = json_product["DrinkName"]
		self.volume =  json_product["Volume"]
		self.id = json_product["_id"]

class listing():
	def __init__(self, json_listing):
		self.expiration = json_listing["Expiration"]
		self.product = product(json_listing["Product"])
		self.seller = json_listing["Seller"]
		self.start_price = json_listing["StartPrice"]
		self.status = json_listing["Status"]
		self.terminating_price = json_listing["TerminatingPrice"]
		self.bids = bids(json_listing["Bids"]) 
		self.type = json_listing["Type"]
		self.id = str(json_listing["_id"])
		self.current_price = self.get_current_price()

	def get_current_price(self):
		if len(self.bids.bid_list) == 0:
			return self.start_price
		else:
			return self.bids.bid_list[-1].bid_amount 

def place_bid(username, listing_id, bid_amount):
	URL = "http://127.0.0.1:23450/bid_service/placeBid?lid="+str(listing_id)+"&uid="+str(username)+"&bid_amt="+str(bid_amount)
	r = requests.get(url = URL)

def get_listings():
	URL = "http://127.0.0.1:5000/getNumberOfListings?num=12"
	r = requests.get(url = URL)
	json_response = r.json()

	listing_objects = []
	for json_listing in json_response['data']:
		pprint.pprint(json_listing)
		listing_objects.append(listing(json_listing))

	return listing_objects

def get_listing_by_id(listing_id):
	URL = "http://127.0.0.1:5000/getListingbyID?reqId=" + str(listing_id)
	r = requests.get(url = URL)
	json_response = r.json()

	print(json_response)

	listing_obj = listing(json_response['data'][0])

	return listing_obj

def create_account(request):
    context = {}
    return render(request, 'auction/create_account.html', context)

def create_account_submit(request):

	first_name = request.POST['first_name']
	username = request.POST['username']
	password = hash(request.POST['password'])

	#TODO: call account service's create account function

	return HttpResponseRedirect(reverse('auction:pending_verification'))

def pending_verification(request):
    context = {}
    return render(request, 'auction/pending_verification.html', context)

def login(request):
    context = {}
    return render(request, 'auction/login.html', context)

def login_submit(request):
	username = request.POST['username']
	password = hash(request.POST['password'])

	#TODO: call account service's login function

	return HttpResponseRedirect(reverse('auction:listings'))

def listings(request):
	listings = get_listings()
	print("========================")
	for listing in listings:
		print(listing.start_price)
	context = {"listings": listings}
	return render(request, 'auction/listings.html', context)

def listing_detail(request, listing_id):
	listing = get_listing_by_id(listing_id)
	listing.bids.bid_list = listing.bids.bid_list[::-1]
	context = {"listing": listing}
	return render(request, 'auction/listing_detail.html', context)

def bid_submit(request):
	username = request.POST['username']
	listing_id = request.POST['listing_id']
	bid_amount = request.POST['bid_amount']

	place_bid(username, listing_id, bid_amount)

	return HttpResponseRedirect(reverse('auction:bid_confirmed'))


def bid_confirmed(request):
    context = {}
    return render(request, 'auction/bid_confirmed.html', context)

def user_account(request):
    context = {}
    return render(request, 'auction/user_account.html', context)

def user_account_submit(request):

	first_name = request.POST['first_name']
	username = request.POST['username']
	password = hash(request.POST['password'])

	#TODO: call account service's create account function

	return HttpResponseRedirect(reverse('auction:pending_verification'))