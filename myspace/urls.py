"""
List of Urls on booking an office space
"""

from django.urls import path, include
from django.contrib import admin
from .views import OfficeList, OfficeBookedList, BookingView,ContactFormView



urlpatterns = [
    path('', OfficeList.as_view(), name='OfficeList'),
    path('office_bookings/', OfficeBookedList.as_view(), name='OfficeBookedList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('contact/', ContactFormView.as_view(), name='Contact'),
] 
