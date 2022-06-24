from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os
import random

# Create your views here.
def index(request):

    pp = pprint.PrettyPrinter(indent=2, depth=2)
    photo_id = request.GET.get('id') or random.randint(1, 9)
    load_dotenv()
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    pp.pprint(auth)
    apikey = (os.environ['apikey'])
    endpoint = f"https://api.unsplash.com/photos/?client_id={apikey}"
    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    photo = responseJSON[int(photo_id)]['urls']['small']
    description = responseJSON[0]['description']
    # pp.pprint(description)
    
    response = render(request, 'pages/index.html', {'preview_url': photo, 'description': description})
    return response

def raw(request):
    photo_id = request.GET.get('id') or random.randint(1, 9)
    load_dotenv()
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    apikey = (os.environ['apikey'])
    endpoint = f"https://api.unsplash.com/photos/?client_id={apikey}"
    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    photo = responseJSON[int(photo_id)]['urls']['raw']
    
    response = render(request, 'pages/index.html', {'preview_url': photo})
    return response

def small(request):
    photo_id = request.GET.get('id') or random.randint(1, 9)
    load_dotenv()
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    apikey = (os.environ['apikey'])
    endpoint = f"https://api.unsplash.com/photos/?client_id={apikey}"
    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    photo = responseJSON[int(photo_id)]['urls']['small']
    
    response = render(request, 'pages/index.html', {'preview_url': photo})
    return response

def thumb(request):
    photo_id = request.GET.get('id') or random.randint(1, 9)
    load_dotenv()
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    apikey = (os.environ['apikey'])
    endpoint = f"https://api.unsplash.com/photos/?client_id={apikey}"
    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    photo = responseJSON[int(photo_id)]['urls']['thumb']
    
    response = render(request, 'pages/index.html', {'preview_url': photo})
    return response