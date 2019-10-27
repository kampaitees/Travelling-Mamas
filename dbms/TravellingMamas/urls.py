from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('layout', views.layout, name = 'layout'),
    path('edit_profile', views.edit_profile, name = 'edit_profle'),
    path('user', views.user, name = 'user'),
    path('profile', views.profile, name = 'profile'),
    path('flight_search', views.flight_search, name = 'flight_search'),
    path('searched_flights', views.searched_flights, name = 'searched_flights'),
    path('booking_flight', views.booking_flight, name = 'booking_flight'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('hotel-room', views.hotel_room, name = 'hotel-room'),
    path('hotels', views.hotels, name = 'hotel'),
    path('services', views.service, name = 'services'),
    # path('tour-place', views.tour_place, name = 'tour-place'),
    path('tours', views.tour, name = 'tours'),
    path('srinagar', views.srinagar, name = 'srinagar'),
    path('shimla', views.shimla, name = 'shimla'),
    path('nainital', views.nainital, name = 'nainital'),
    path('darjeeling', views.darjeeling, name = 'darjeeling'),
    path('coorg', views.coorg, name = 'coorg'),
    path('ooty', views.ooty, name = 'ooty'),
    path('alleppey', views.alleppey, name = 'alleppey'),
    path('dharmashala', views.dharmashala, name = 'dharmashala'),
    path('kashmir',views.kashmir, name = 'kashmir'),
    path('shimla_main',views.shimla_main, name = "shimla_main"),
    path('nainital_main',views.nainital_main, name = 'nainital_main'),
    path('darjeeling_main',views.darjeeling_main, name = 'darjeeling_main'),
    path('coorg_main', views.coorg_main, name = 'coorg_main'),
    path('ooty_main', views.ooty_main, name = 'ooty_main'),
    path('alleppey_main', views.alleppey_main, name = 'alleppey_main'),
    path('dharamshala_main', views.dharamshala_main, name = 'dharamshala_main'),
    path('three', views.three, name = 'three'),
    path('two', views.two, name = 'two'),
    path('hotel_booking', views.hotel_booking, name = 'hotel_booking'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('password_reset', PasswordResetView.as_view(template_name = 'password_reset.html'), name = 'password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete')
]
