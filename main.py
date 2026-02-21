import fastapi
from mysite.api import userprofile, service, room_image, room, review, booking, city, country, hotel_image, hotel, auth
import uvicorn
# from mysite.database.db import engine
from mysite.admin.setup import setup_admin


# Вот структура папок с картинки:
#
# - `nginx`
# - `.env`
# - `alembic.ini`
# - `docker-compose.yml`
# - `Dockerfile`
# - `main.py`
# - `req.txt`
#


booking_app = fastapi.FastAPI(title='Store Project')

setup_admin(booking_app)
booking_app.include_router(userprofile.userprofile_router)
booking_app.include_router(service.service_router)
booking_app.include_router(room_image.room_image_router)
booking_app.include_router(room.room_router)
booking_app.include_router(review.review_router)
booking_app.include_router(booking.booking_router)
booking_app.include_router(country.country_router)
booking_app.include_router(hotel.hotel_router)
booking_app.include_router(hotel_image.hotel_image_router)
booking_app.include_router(auth.auth_router)

if __name__ == '__main__':
    uvicorn.run(booking_app, host='127.0.0.1', port=8000)