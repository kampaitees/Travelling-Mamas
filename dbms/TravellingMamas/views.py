from django.shortcuts import render
from django.http import HttpResponse
from . import models  
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def hotel_room(request):
    return render(request, 'hotel-room.html')

def hotels(request):
    return render(request, 'hotels.html')

def service(request):
    return render(request, 'services.html')

# def tour_place(request):
#     return render(request, 'tour_place.html')

def tour(request):
    return render(request, 'tours.html')

def srinagar(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[:8]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'srinagar.html', {'list' : list_hotels})

def shimla(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[8:16]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'shimla.html', {'list' : list_hotels})

def nainital(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[16:24]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    print(list_hotels)
    return render(request, 'nainital.html', {'list' : list_hotels})

def darjeeling(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[24:32]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'darjeeling.html', {'list' : list_hotels})

def coorg(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[32:40]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'coorg.html', {'list' : list_hotels})


def ooty(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[40:48]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'ooty.html', {'list' : list_hotels})

def alleppey(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[48:56]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'alleppey.html', {'list' : list_hotels})


def dharmashala(request):
    list_hotels = []
    hotels = models.hotel.objects.all()
    hotels = hotels[56:64]
    price = [1430, 1320, 1200, 1078, 2130, 4535, 2120, 5450]
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    random.shuffle(price)
    for hotel, price in zip(hotels, price):
        list_hotels.append((hotel, price))
    return render(request, 'dharmashala.html', {'list' : list_hotels})

def kashmir(request):
    return render(request, 'kashmir.html')

def shimla_main(request):
    return render(request, 'shimla_main.html')

def nainital_main(request):
    return render(request, 'nainital_main.html')

def darjeeling_main(request):
    return render(request, 'darjeeling_main.html')

def coorg_main(request):
    return render(request, 'coorg_main.html')

def ooty_main(request):
    return render(request, 'ooty_main.html')

def alleppey_main(request):
    return render(request, 'alleppey_main.html')

def dharamshala_main(request):
    return render(request, 'dharamshala_main.html')

def three(request):
    return render(request, 'three.html')

def two(request):
    return render(request, 'two.html')


def hotel_booking(request):
    return render(request, 'hotel_booking.html')