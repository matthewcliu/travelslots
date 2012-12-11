from django import forms

class SearchForm(forms.Form):
    departure_date = forms.CharField(max_length=256, required = True)
    return_date = forms.CharField(max_length=256, required = False)        
    departure_airport = forms.CharField(max_length=256, required = False)