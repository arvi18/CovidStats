from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.urls.base import get_script_prefix
import requests


def index(request):
    result = requests.get('https://api.covid19india.org/data.json')
    countrySummary = result.json()['cases_time_series']
    india = countrySummary[-1]

    result2 = requests.get(
        "https://api.covid19india.org/state_district_wise.json")
    maha = result2.json()['Maharashtra']['districtData']
    pune = maha["Pune"]
    Thane = maha["Thane"]
    Mumbai = maha["Mumbai"]
    Nashik = maha["Nashik"]
    Nagpur = maha["Nagpur"]

    result = requests.get('https://api.covid19india.org/data.json')
    stateSummary = result.json()['statewise']
    mh = [item for item in stateSummary if item["state"] == "Maharashtra"][0]

    return render(request, 'dataApp/index.html', {'maha': maha, "india": india, 'mh': mh, 'pune': pune, 'Thane': Thane, 'Mumbai': Mumbai, 'Nashik': Nashik, 'Nagpur': Nagpur})
