"""
List of Urls on booking an office space
"""

from django.urls import path
from .views import OfficeList, OfficeBookedList, BookingView


urlpatterns = [
    path('office_list/', OfficeList.as_view(), name='offices'),
    path('office_bookings/', OfficeBookedList.as_view(), name='bookings'),
    path('book/', BookingView.as_view(), name='booking_view')
]
