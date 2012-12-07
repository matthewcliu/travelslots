# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import jsonrpclib
from travelslots.constants import *

# Create your views here.
def index(request):

    user_departure_date = "2012-12-10"
    user_return_date = "2012-12-20"
    journeys_to_display = everbread_query(AIRPORTS_TO_QUERY, user_departure_date, user_return_date)
    params = {'journeys_to_display':journeys_to_display}
    return render_to_response('index.html', params)
    
def everbread_query(airports_to_query, departure_date, return_date):
    service_url = EVERBREAD_SERVICE_URL 
    proxy = jsonrpclib.Server(service_url)

    aggregated_journeys = []
    
    for airport in airports_to_query:

        everbread_request = {  
            "user": EVERBREAD_USER,
            "pass": EVERBREAD_PASSWORD,
            "departure": DEPARTURE_AIRPORT,
            "arrival": airport,
            "departureDate": departure_date,
            "returnDate": return_date,
            "airline": "",
            "directFlightsOnly": True
        }
                
        try:
            everbread_response = proxy.search(everbread_request)
            everbread_journeys = everbread_response['journeys']            
            aggregated_journeys += everbread_journeys

        except:
            print "Error connecting to Miniapi service!"

    return aggregated_journeys
    