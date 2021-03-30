from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render

def create_account(request):
    context = {}
    return render(request, 'auction/create_account.html', context)

def login(request):
    context = {}
    return render(request, 'auction/login.html', context)

def login_submit(request):
	username = request.POST['username']
	password = request.POST['password']

	return HttpResponseRedirect(reverse('auction:listings'))



def listings(request):
    context = {}
    return render(request, 'auction/listings.html', context)

def listing_detail(request, listing_id):
    context = {"listing_id": listing_id}
    return render(request, 'auction/listing_detail.html', context)