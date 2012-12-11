from django import forms

class SearchForm(forms.Form):
    departure_date = forms.CharField(max_length=32, required = True)
    return_date = forms.CharField(max_length=32, required = True)        
    departure_airport = forms.CharField(max_length=32, required = True)