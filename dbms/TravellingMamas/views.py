import random
from . import models  
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username = user_name, first_name = first_name, last_name = last_name, email = email, password = password)
                user.save()
                messages.info(request, "User created Successfully")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')

        return redirect('register')
    
    
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username = user_name, password = password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


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