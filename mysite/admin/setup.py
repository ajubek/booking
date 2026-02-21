from .views import (CountryAdmin, UserProfileAdmin, CityAdmin, ServiceAdmin, HotelAdmin,
                    HotelImageAdmin, RoomImageAdmin, ReviewAdmin, BookingAdmin)
from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine

def setup_admin(mysite: FastAPI):
    admin = Admin(mysite, engine)
    admin.add_view(CountryAdmin)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CityAdmin)
    admin.add_view(ServiceAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(HotelImageAdmin)
    admin.add_view(RoomImageAdmin)
    admin.add_view(ReviewAdmin)
    admin.add_view(BookingAdmin)