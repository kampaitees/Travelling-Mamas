create table hotel(
    hotel_id varchar(100) primary key,
    hotel_name varchar(100),
    description varchar(100), 
    location varchar(100),
    reviews int
);

create table tour(
    tour_id varchar(100) primary key,
    tour_name varchar(100),
    fare integer, 
    place varchar(100),
    location varchar(100),
    reviews integer,
    description varchar(100)
);

create table flight(
    flight_number varchar(100) primary key,
    origin varchar(100),
    departure_time varchar(100), 
    place varchar(100),
    arrival_time varchar(100),
    destination varchar(100)
);

-- create table book(
--     user_id varchar(100),
--     flight_number varchar(100),
--     hotel_id varchar(100),
--     tour_id varchar(100),
--     primary key (user_id, flight_number, hotel_id, tour_id),
--     foreign key (user_id) references user(user_id),
--     foreign key (flight_number) references flight(flight_number),
--     foreign key (hotel_id) references hotel(hotel_id),
--     foreign key (tour_id) references tour(tour_id)
-- );



-- create table class (
--     flight_number varchar(100), 
--     type varchar(100),
--     primary key(flight_number, type)
-- );


-- create table belong_to (
--     airline_id varchar(100),
--     flight_number varchar(100),
--     primary key (airline_id, flight_number),
--     foreign key (airline_id) references airline(airline_id),
--     foreign key (flight_number) references flight(flight_number)
-- );

-- create table consists (
--     hotel_id varchar(100),
--     room_id varchar(100),
--     primary key(hotel_id, room_id),
--     foreign key (hotel_id) references hotel(hotel_id),
--     foreign key (room_id) references rooms(room_id)
-- );

create table room_type (
    room_number varchar(100),
    room_id varchar(100),
    price integer,
    primary key(room_id, room_number)
);

-- create table rooms(
--     room_id varchar(100) primary key,
--     accomadation varchar(100)
-- );

-- create table has_flight(
--     flight_number varchar(100),
--     type varchar(100),
--     primary key(flight_number, type)
-- );

-- alter table has_flight add constraint fk_has_flight_flight foreign key (flight_number) references flight(flight_number);
-- alter table has_flight add constraint fk_has_flight_flight foreign key (flight_number, type) references class(flight_number, type);

-- create table has_room(
--     room_id varchar(100),
--     room_number varchar(100),
--     primary key(room_number, room_id)
-- );


-- alter table has_room add constraint fk_has_room_rooms foreign key (room_id) references rooms(room_id);
-- alter table has_room add constraint fk_has_room_room_type foreign key (room_id, room_number) references room_type(room_id, room_number);

-- create table airline(
--     airline_id varchar(100) primary key,
--     name varchar(100),
--     head_quarter_city varchar(100)
-- );

-- create table contact(
--     user_id varchar(100) primary key,
--     contact varchar(100)
-- );

create table user(
    user_id varchar(100),
    email varchar(100),
    first_name varchar(100),
    middle_name varchar(100),
    last_name varchar(100),
    password varchar(100),
    dob varchar(100),
    primary key (user_id, email)
);

