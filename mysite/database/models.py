from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey,  Text,  DateTime
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime

class StatusChoices(str, PyEnum):
    client = 'client'
    owner = 'owner'

class RoomStatusChoices(str,PyEnum):
    Occupied = "Occupied"
    Reserved = "Reserved"
    Available = "Available"



class RoomTypeChoices(str,PyEnum):
    luxury = "luxury"
    junior_suite = "junior_suite"
    Family = "Family"
    Economy = "Economy"
    Single = "Single"


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_name: Mapped[str] = mapped_column(String(30), unique=True)
    country_image: Mapped[str] = mapped_column(String)
    user_country: Mapped[List['UserProfile']] = relationship(back_populates='country', cascade='all, delete-orphan')
    hotel_country: Mapped[List['Hotel']] = relationship(back_populates='country_hotel', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.country_name}'



class UserProfile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.client)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)
    country_id: Mapped[Optional[int]] = mapped_column(ForeignKey('country.id'), nullable=True)  # ← добавь

    country: Mapped[Optional['Country']] = relationship(back_populates='user_country')
    owner_hotel: Mapped[List['Hotel']] = relationship(back_populates='owner', cascade='all, delete-orphan')
    user_reviews: Mapped[List['Review']] = relationship(back_populates='user_rev', cascade='all, delete-orphan')
    booking_user: Mapped[List['Booking']] = relationship(back_populates='user_booking', cascade='all, delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}'






class City(Base):
    __tablename__ = 'city'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    city_name: Mapped[str] = mapped_column(String(100))
    city_image: Mapped[str] = mapped_column(String)

    hotel_city: Mapped[List['Hotel']] = relationship(back_populates='city_hotel')

    def __repr__(self):
        return f'{self.city_name}'


class Service(Base):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    service_image: Mapped[str] = mapped_column(String, nullable=True)
    service_name: Mapped[str] = mapped_column(String(30))

    hotel_service: Mapped[List['Hotel']] = relationship(back_populates='services', cascade='all, delete-orphan')



class Hotel(Base):
    __tablename__ = 'hotel'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'))
    country_hotel: Mapped[Country] = relationship(back_populates='hotel_country')
    hotel_name: Mapped[str] = mapped_column(String(50))
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'))
    city_hotel: Mapped[City] = relationship(back_populates='hotel_city')
    street: Mapped[str] = mapped_column(String(50))
    postal_code: Mapped[int] = mapped_column(Integer)
    hotel_stars: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    owner_id: Mapped[UserProfile] = mapped_column(ForeignKey('profile.id'))
    owner: Mapped[UserProfile] = relationship(UserProfile, back_populates='owner_hotel')
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'))

    services: Mapped[Service] = relationship(back_populates='hotel_service')
    image_hotel: Mapped[List['HotelImage']] = relationship(back_populates='hotel_image', cascade='all, delete-orphan')
    room_hotel: Mapped[List['Room']] = relationship(back_populates='hotel_room', cascade='all, delete-orphan')
    hotel_reviews: Mapped[List['Review']] = relationship(back_populates='hotel_rev', cascade='all, delete-orphan')
    booking_hotel: Mapped[List['Booking']] = relationship(back_populates='hotel_booking', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.hotel_name}'


class HotelImage(Base):
    __tablename__ = 'hotel_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    hotel_image: Mapped[Hotel] = relationship(Hotel, back_populates='image_hotel')


class Room(Base):
    __tablename__ = 'room'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    price: Mapped[int] = mapped_column(Integer)
    room_number: Mapped[int] = mapped_column(Integer)
    room_status: Mapped[RoomStatusChoices] = mapped_column(Enum(RoomStatusChoices), default=RoomStatusChoices.Occupied)
    room_type: Mapped[RoomTypeChoices] = mapped_column(Enum(RoomTypeChoices), default=RoomTypeChoices.Single)
    description: Mapped[str] = mapped_column(Text)

    hotel_room: Mapped[Hotel] = relationship(Hotel, back_populates='room_hotel')
    image_room: Mapped[List['RoomImage']] = relationship(back_populates='room_image', cascade='all, delete-orphan')
    booking_room: Mapped[List['Booking']] = relationship(back_populates='room_booking', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.room_type}'

class RoomImage(Base):
    __tablename__ = 'room_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    room_image: Mapped[str] = relationship(Room, back_populates='image_room')
    image: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f'{self.room},{self.room_image}'


class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    stars: Mapped[int] = mapped_column(Integer)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    comment: Mapped[str] = mapped_column(Text, nullable=True)



    hotel_rev: Mapped[Hotel] = relationship(back_populates='hotel_reviews')
    user_rev: Mapped[UserProfile] = relationship(back_populates='user_reviews')



    def __repr__(self):
        return f'{self.text}'

class Booking(Base):
    __tablename__ = 'booking'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    check_in: Mapped[date] = mapped_column(Date,default=date.today())
    check_out: Mapped[date] = mapped_column(Date, default=date.today())
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    user_booking: Mapped[UserProfile] = relationship(back_populates='booking_user')
    room_booking: Mapped[Room] = relationship(back_populates='booking_room')
    hotel_booking: Mapped[Hotel] = relationship(back_populates='booking_hotel')





class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')



    def __repr__(self):
        return f'{self.token}'