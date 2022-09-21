from django.shortcuts import render
import requests


def us_forecast(request):
    return render(request, 'weather/index.html')