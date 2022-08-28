from .views import OfficeList, OfficeBookedList
from django.urls import path

urlpatterns = [
    path('office_list/', OfficeList().as_view(), name='officelist'),
    path('office_bookings/', OfficeBookedList().as_view(), name='officebookings'),
]
