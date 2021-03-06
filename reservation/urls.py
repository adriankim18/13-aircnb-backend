from django.urls import path
from reservation.views import Reservation, Cancellation

urlpatterns = [
    path('/booking', Reservation.as_view()),
    path('/cancellation/<int:booking_id>', Cancellation.as_view()),
]
