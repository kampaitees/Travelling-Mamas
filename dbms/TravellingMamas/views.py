import time
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




def hotel_booking(request):
    
    list_of_hotels = ['Hotel Woodpark', 'Hotel Novacany', 'Hotel Madaland', 'Hotel Sanskriti', 'Hotel Sriram resort', 'Hotel Rishi Mangalam',
                  'Hotel Rosewood International', 'Hotel Basant Residency', 'Hotel Sharma Brothers', 'Hotel Havetual', 'Hotel Sankriti', 
                  'Hotel Ganga', 'Hotel American Resort', 'Hotel Mountain Crest', 'Hotel Snow Queen', 'Hotel Radisan', 'Hotel Pythava Resort', 
                  'Hotel Wild Ville', 'Hotel Sansar Apna', 'Hotel Appleview', 'Hotel Polish Resort', 'Hotel Hirest', 'Hotel King Resort',
                  'Hotel Nishu', 'Hotel Rista Resort', 'Hotel Nature Ville', 'Hotel Sansar', 'Hotel Pineview', 'Hotel British Resort', 
                  'Hotel Hill Crest', 'Hotel Snow King Resort', 'Hotel Nishat', 'Hotel Raj Resort', 'Hotel Abbydhama Esate Stay', 
                  'Hotel Woodstack Villa', 'Hotel Coorg Heights', 'Hotel Indrastha', 'Hotel IBNI', 'Hotel OYO Hilldale Resort', 'Hotel Vashati', 
                  'Hotel Fabkhems', 'Hotel Treebo Trend Whispering', 'Hotel Novacany', 'Hotel Sterling', 'Hotel LakeView', 'Hotel Sunaark Grand',
                  'Hotel Tuilips', 'Hotel Berry Hills', 'Hotel WhiteShore Beach', 'Hotel Ramada', 'Hotel Baywatch Beach Resort', 
                  'Hotel Paagada Resort', 'Hotel Royal Park', 'Hotel Zostel', 'Hotel Bamboon Lagoon', 'Hotel Palace Resort', 'Hotel Adhivaha',
                  'Hotel Vaikunth', 'Hotel InClover', 'Hotel Pink Resorts', 'Hotel Dauladhar', 'Hotel Zostel', 'Hotel Horizon Villa', 
                  'Hotel Imperial Resorts']
    list_of_hotels = [i.lower() for i in list_of_hotels] 
    list_of_rooms = ['FAMILY ROOM', 'DOUBLE ROOM', 'SUITE ROOM', 'LUXURY ROOM', 'CLASSICAL DOUBLE ROOM', 'CLASSICAL DOUBLE ROOM']
    list_of_rooms = [i.lower() for i in list_of_rooms]

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_number = request.POST['number']
        check_in = request.POST['in']
        check_out = request.POST['out']
        number_of_guests = request.POST['number_of_guests']
        room_type = request.POST['room_type']
        hotel_name = request.POST['hotel_name']
        user_id = request.user.id

        if len(mobile_number) != 10:
            messages.info(request, "Mobile number should be 10 digit")
            return redirect('hotel_booking')

        elif check_out < check_in:
            messages.info(request, "Check-in  can't be greater than Check-out")
            return redirect('hotel_booking')

        elif room_type.lower() not in list_of_rooms:
            print(room_type.lower())
            messages.info(request, "Above Room Type is not available")
            return redirect('hotel_booking')

        elif hotel_name.lower() not in list_of_hotels:
            messages.info(request, "Invalid Hotel Name")
            return redirect('hotel_booking')
        else:   
            models.user_details.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                room_type = room_type,
                hotel_name = hotel_name,
                check_in = check_in,
                check_out = check_out,
                number_of_guests = number_of_guests,
                mobile_number = mobile_number,
                user_id = user_id
            )
            messages.info(request, "Booked Successfully")
            time.sleep(5)
            return redirect('/')

    else:
        return render(request, 'hotel_booking.html')


def flight_search(request):
    flights = models.flight_prime.objects.all()
    list_of_eligible_flights, list_of_eligible_return_flights = [], []
    if request.method == 'POST':
        source_city = request.POST['source_city']
        destination_city = request.POST['destination_city']
        departure_date = request.POST['departure_date']
        return_date = request.POST.get('return_date')
        round_depart_checkbox = request.POST.get('round_depart_checkbox')
        round_return_checkbox = request.POST.get('round_return_checkbox')
        oneway_depart_checkbox = request.POST.get('oneway_depart_checkbox')
        # print(return_date, round_depart_checkbox, round_return_checkbox)
        if return_date is None:
            for flight in flights:
                if oneway_depart_checkbox is None:        
                    if flight.source == source_city and flight.destination == destination_city and flight.date == departure_date:
                        list_of_eligible_flights.append(flight)
                        # print(list_of_eligible_flights, class_type)
                else:
                    if flight.source == source_city and flight.destination == destination_city and flight.date >= departure_date:
                        list_of_eligible_flights.append(flight)
                        # print(list_of_eligible_flights)
                
            return render(request, 'searched_flights.html', {'value' : 0, 'flights':list_of_eligible_flights})
        else:
            for flight in flights:
                if round_depart_checkbox is None:  
                    if flight.source == source_city and flight.destination == destination_city and flight.date == departure_date:
                        list_of_eligible_flights.append(flight)
                        # print(list_of_eligible_flights)
                else:
                    if flight.source == source_city and flight.destination == destination_city and flight.date >= departure_date:
                        list_of_eligible_flights.append(flight)
                        # print(list_of_eligible_flights)

                if round_return_checkbox is None: 
                    if flight.source == destination_city and flight.destination == source_city and flight.date == return_date:
                        list_of_eligible_return_flights.append(flight)
                        # print(list_of_eligible_return_flights)
                else:
                    if flight.source == destination_city and flight.destination == source_city and flight.date >= return_date:
                        list_of_eligible_return_flights.append(flight)
                        # print(list_of_eligible_return_flights)
            
            # print(list_of_eligible_flights)
            # print(list_of_eligible_return_flights)
            return render(request, 'searched_flights.html', {'value' : 1, 'depart' : list_of_eligible_flights, 'return' : list_of_eligible_return_flights})

    else:
        return render(request, 'flight_search.html')


def booking_flight(request):
    if request.method == 'POST':
        source_city = request.POST['source_city']
        destination_city = request.POST['destination_city']
        airline = request.POST['airline']
        seat_type = request.POST['seating']
        departure_date = request.POST['date']
        adult_count = request.POST['adult_count']
        child_count = request.POST['child_count']
        fullname = request.POST['name']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        user_id = request.user.id

        if len(mobile_number) != 10:
            messages.info(request, "Mobile number should be 10 digit")
            return redirect('booking_flight')
       
        else:   
            models.user_flight_details.objects.create(
                source_city = source_city,
                destination_city = destination_city,
                airline = airline,
                seat_type = seat_type,
                departure_date = departure_date,
                adult_count = adult_count,
                child_count = child_count,
                fullname = fullname,
                mobile_number = mobile_number,
                email = email,
                user_id = user_id
            )
            messages.info(request, "Booked Successfully")
            # time.sleep(3)
            return redirect('/')

    else:
        return render(request, 'booking_flight.html')

def user(request):
    return render(request, 'user.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def layout(request):
    return render(request, 'layout.html')


def profile(request):
    return render(request, 'profile.html')


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

