# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
import jsonrpclib
from travelslots.constants import *
from search_form import *

# Create your views here.
def index(request):

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            departure_date = search_form.cleaned_data['departure_date']
            return_date = search_form.cleaned_data['return_date']
            departure_airport = search_form.cleaned_data['departure_airport']
            journeys_to_display = everbread_query(AIRPORTS_TO_QUERY, departure_date, return_date, departure_airport)
            params = {'search_form': search_form, 'journeys_to_display':journeys_to_display}
            #return render_to_response('index.html', params)
            return render(request,'index.html', params)
    else:
        search_form = SearchForm()
    
    return render(request, 'index.html', {'search_form': search_form})

    
def everbread_query(airports_to_query, departure_date, return_date, departure_airport):
    service_url = EVERBREAD_SERVICE_URL 
    proxy = jsonrpclib.Server(service_url)

    aggregated_journeys = []
    
    for airport in airports_to_query:

        everbread_request = {  
            "user": EVERBREAD_USER,
            "pass": EVERBREAD_PASSWORD,
            "departure": departure_airport,
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