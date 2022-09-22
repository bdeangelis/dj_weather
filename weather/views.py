from django.shortcuts import render
from django.contrib import messages
from .forms import GetWeather
import requests
from geopy.geocoders import Nominatim
from datetime import date, timedelta
    


def get_forecast(address: str, city: str, state: str, zip_code: str, country: str)-> dict:
    """
    GIVEN the weather api
    WHEN address is included in the url
    THEN a 5 day forecast object is returned
    """
    # Ideally this key would be placed in a secure store not held in the repo
    API_KEY = 'W8SCBDW9X9DRXWNZSYZEUUVFN'
    today = date.today()
    plus_5_days = today + timedelta(days=4)
    full_address = f"{address} {city} {state} {zip_code} {country}"
    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{full_address}/{today}/{plus_5_days}?unitGroup=us&include=days&key={API_KEY}&contentType=json'
    api_request = requests.get(url=URL)
    api_response_json = api_request.json()
    return api_response_json


def us_forecast(request):
    """
    GIVEN the users address is entered in the form
    WHEN that info is submitted to the weather api
    THEN a 5 day high/low is returned for the location 
    """
    
    if request.method == 'POST':
        form = GetWeather(request.POST)
        
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip']
            country = form.cleaned_data['country']
            forecast = get_forecast(address, city, state, zip_code, country)
            days_list = forecast.get('days')
            resolved_address = forecast.get('resolvedAddress')
            return render(request, 'weather/forecast.html', {'forecast':days_list, 'address': resolved_address})

    else:
        form = GetWeather()

    return render(request, 'weather/index.html', {'form':form})