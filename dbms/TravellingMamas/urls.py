from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('hotel-room', views.hotel_room, name = 'hotel-room'),
    path('hotels', views.hotels, name = 'hotel'),
    path('services', views.service, name = 'services'),
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
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('password_reset', PasswordResetView, name = 'password_reset'),
    path('password_reset/done', PasswordResetDoneView, name = 'password_reset_done')
]
