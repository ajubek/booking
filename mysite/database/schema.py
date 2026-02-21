from pydantic import BaseModel, EmailStr
from typing import Optional
from .models import StatusChoices
from datetime import date, datetime





class CountryInputSchema(BaseModel):
    country_name:str
    country_image:str


class CountryOutSchema(BaseModel):
    id: int
    country_name: str
    country_image: str


class UserLoginShema(BaseModel):
    username: str
    password: str



class UserProfileInputSchema(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    password:str
    age:Optional[int]
    phone_number:Optional[str]
    country_id:int



class UserProfileOutSchema(BaseModel):
    id:int
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    password:str
    age:Optional[int]
    phone_number:Optional[str]
    country_id:int





class CityInputSchema(BaseModel):
    city_name:str
    city_image:str




class CityOutSchema(BaseModel):
    id:int
    city_name:str
    city_image:str



class ServiceInputSchema(BaseModel):
    service_image:str
    service_name:str




class ServiceOutSchema(BaseModel):
    id:int
    service_image:str
    service_name:str


class HotelInputSchema(BaseModel):
    country_id: int
    hotel_name: str
    city_id: int
    street: str
    postal_code: int
    hotel_stars: int
    description: str
    service_id: int


class HotelOutSchema(BaseModel):
    id:int
    country_id:int
    hotel_name:str
    city_id:int
    street:str
    postal_code:int
    hotel_stars:int
    description:str
    service_id:int


class HotelImageInputSchema(BaseModel):
    hotel_id:str



class HotelImageOutSchema(BaseModel):
    id:int
    hotel_id:str


class RoomInputSchema(BaseModel):
    hotel_id:int
    price:int
    room_number:int
    room_status:StatusChoices
    room_type:StatusChoices
    description:str



class RoomOutSchema(BaseModel):
    id: int
    hotel_id:int
    price:int
    room_number:int
    room_status:StatusChoices
    room_type:StatusChoices
    description:str


class RoomImageInputSchema(BaseModel):
    room_id:int
    room_image:str
    image:str


class RoomImageOutSchema(BaseModel):
    id:int
    room_id:int
    room_image:str
    image:str


class ReviewInputSchema(BaseModel):
    user_id:int
    hotel_id:int
    stars:int
    created_date:datetime
    comment:str



class ReviewOutSchema(BaseModel):
    id:int
    user_id:int
    hotel_id:int
    stars:int
    created_date:datetime
    comment:str


class BookingInputSchema(BaseModel):
    user_id: int
    room_id: int
    hotel_id: int
    check_in: date
    check_out: date
    created_date: datetime



class BookingOutSchema(BaseModel):
    id:int
    user_id:int
    room_id:int
    hotel_id:int
    check_in:date
    check_out:date
    created_date:datetime



class RefreshTokenInputSchema(BaseModel):
    user_id:int
    token:str
    created_date:datetime




