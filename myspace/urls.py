"""
List of Urls on booking an office space
"""

from django.urls import path, include
from django.contrib import admin
from .views import OfficeList, OfficeBookedList, BookingView,ContactFormView, delete_office_booking
from . import views 



urlpatterns = [
    path('', OfficeList.as_view(), name='OfficeList'),
    path('office_bookings/', OfficeBookedList.as_view(), name='OfficeBookedList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('contact/', ContactFormView.as_view(), name='Contact'),
    path('delete_office_booking/<booking_id>', views.delete_office_booking, name='delete_office_booking'),  


] 
