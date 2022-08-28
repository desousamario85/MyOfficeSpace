from django.urls import path
from .views import OfficeList as OL
from .views import OfficeBookingList as OBL

app_name = 'myspace'

urlpatterns = [
    path('office_list/', OL().as_view(), name='OL'),
    path('office_bookings_list/', OBL().as_view(), name='OBL'),
]
