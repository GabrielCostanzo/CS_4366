from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render
import requests
import pprint

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
		#self.bids = json_listing[""] 
		self.type = json_listing["Type"]
		self.id = str(json_listing["_id"])

def get_listings():
	URL = "http://127.0.0.1:5000/getNumberOfListings?num=12"
	r = requests.get(url = URL)
	json_response = r.json()

	listing_objects = []
	for json_listing in json_response['data']:
		pprint.pprint(json_listing)
		listing_objects.append(listing(json_listing))

	return listing_objects


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
	context = {"listing_id": listing_id}
	return render(request, 'auction/listing_detail.html', context)