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
    lst=[]
    noofresults=int(response['results'])

    for x in range(0,noofresults):
        lst.append(response['response'][x]['country'])

    if request.method=='POST':
        scountry=request.POST['selectedcountry']
        print(scountry)
        noofresults=int(response['results'])
        for x in range(0,noofresults):
            if scountry==response['response'][x]['country']:
                active=response['response'][x]['cases']['active']
                new=response['response'][x]['cases']['new']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        d={'lst':lst,'scountry':scountry,'new':new,'active':active,'recovered':recovered,'critical':critical,'total':total,'deaths':deaths}
        return render(request,'index.html',d)

    
    d={'lst':lst}
    return render(request,'index.html',d)

