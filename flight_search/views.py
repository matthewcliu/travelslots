# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    params = {}
    return render_to_response('index.html', params) # Redirect after POST
    