from django.db import models

# Create your models here.
class hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reviews = models.IntegerField()

class tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    tour_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fare = models.IntegerField()
    reviews = models.IntegerField()

class flight(models.Model):
    flight_number = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.TimeField(blank=True)
    departure_time = models.TimeField(blank=True)

class room_type(models.Model):
    class Meta:
        unique_together = (('room_number', 'room_id'),)

    room_id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    price = models.IntegerField()



class user(models.Model):
    class Meta:
        unique_together = (('user_id', 'email'),)

    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField(blank=True)


class contact(models.Model):
	user_id = models.AutoField(primary_key=True)
	contact = models.IntegerField()


class rooms(models.Model):
	room_id = models.AutoField(primary_key=True)
	accomadation = models.IntegerField()

class airline(models.Model):
	airline_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	head_quarter_city = models.CharField(max_length=100)

class hotel_class(models.Model):
    flight_number = models.AutoField(primary_key=True)
    type = models.CharField(max_length = 100)

class has_flight(models.Model):
    class Meta:
        unique_together = (('flight_number', 'type'),)

    flight_number = models.IntegerField()
    type = models.CharField(max_length=100)
    flight_number = models.ForeignKey(flight, on_delete=models.CASCADE)
    type = models.ForeignKey(hotel_class, on_delete=models.CASCADE)

class has_room(models.Model):
    class Meta:
        unique_together = (('room_id', 'room_number'),)

    room_id = models.IntegerField()
    room_number = models.IntegerField()
    room_id = models.ForeignKey(rooms, on_delete=models.CASCADE)
    room_number = models.ForeignKey(room_type, on_delete=models.CASCADE)


class belong_to(models.Model):
	class Meta:
		unique_together = (('airline_id','flight_number'),)

	airline_id = models.IntegerField()
	flight_number = models.IntegerField()
	airline_id = models.ForeignKey(airline, on_delete=models.CASCADE)
	flight_number = models.ForeignKey(flight, on_delete=models.CASCADE)


class consists(models.Model):
    class Meta:
        unique_together = (('hotel_id', 'room_id'),)

    hotel_id = models.IntegerField()
    room_id = models.IntegerField()
    hotel_id = models.ForeignKey(hotel, on_delete=models.CASCADE)
    room_id = models.ForeignKey(room_type, on_delete=models.CASCADE)

class book(models.Model):
    class Meta:
        unique_together = (('user_id', 'flight_number', 'hotel_id', 'tour_id'),)

    user_id = models.IntegerField()
    flight_number = models.IntegerField()
    hotel_id = models.IntegerField()
    tour_id = models.IntegerField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(flight, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(hotel, on_delete=models.CASCADE)
    tour_id = models.ForeignKey(tour, on_delete=models.CASCADE)