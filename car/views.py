from urllib import response
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
import requests
import time
from car.models import car_id, car_details
from datetime import datetime


def index(response):
    car_id.objects.all().delete()
    for c in range(1, 10):
        request = requests.get('http://cubito.co.in/cab-location-assignment/')
        data = request.json()
        b = car_id()
        b.Trip = data['trip_id']
        b.save()
        all_car = car_id.objects.all()

    return render(response, 'car/index.html', {'all_car': all_car})


def details(request):
    tstart = datetime.now()
    tstop = datetime.now()
    state = "RUNNING"
    if request.method == "POST":
        print(request.POST)
        lr_name = request.POST['lol']
        while state == "RUNNING":
            b = car_id.objects.get(id=lr_name)
            name = b.Trip
            a = car_details()
            a.Trip_name = b
            real_data = requests.get("http://cubito.co.in/cab-location-assignment/?trip_id=" + b.Trip)
            data = real_data.json()
            a.Status = data['status']
            a.TimeDate = data['lastupdate']
            state = a.Status
            if tstart > tstop:
                tstart = datetime.now()
            tstop = datetime.now()
            a.Map = data['map']
            a.Lat = data['location']['latitude']
            a.Long = data['location']['longitude']
            a.save()
    all_car = car_id.objects.all()
    ok = car_details.objects.all()
    diff = tstop - tstart
    duration = divmod(diff.days * 86400 + diff.seconds, 60)
    context = {
        "map_points": ok,
        "all_car": all_car,
        "tstart": tstart,
        "tstop": tstop,
        "duration": duration,
        "name":name,
    }

    return render(request, 'car/details.html', context)

