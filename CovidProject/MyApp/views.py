from django.shortcuts import render,HttpResponse
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "b7ef0e1730msh15273a09ee3fdedp1e34b5jsnf8250eec58a4",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
# Create your views here.
def home(request):
    noofresults=int(response['results'])
    lst=[]
    for x in range(0,noofresults):
        lst.append(response['response'][x]['country'])
    d={'lst':lst}
    return render(request,'index.html',d)

