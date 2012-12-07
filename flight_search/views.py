# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import jsonrpclib
from travelslots.constants import *



# Create your views here.
def index(request):
    
    service_url = EVERBREAD_SERVICE_URL 
    proxy = jsonrpclib.Server(service_url)

    request = {  
        "user": EVERBREAD_USER,
        "pass": EVERBREAD_PASSWORD,
        "departure": DEPARTURE_CITY,
        "arrival": "LON",
        "departureDate": "2012-12-10",
        "returnDate": "2012-12-20",
        "airline": "",
        "directFlightsOnly": True
    }

    try:
        response = proxy.search(request)

        journeys = response['journeys']

        for j in range(len(journeys)):
            print "Journey: %s %s" % (j+1, journeys[j])
    except:
        print "Error connecting to Miniapi service!"
    
    params = {'journeys':journeys}
    return render_to_response('index.html', params) # Redirect after POST
    