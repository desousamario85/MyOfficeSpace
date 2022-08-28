from django.shortcuts import render
from django.views.generic import ListView
from .models import Office_Spaces,Office_Spaces_Booked

# Create your views here.

class OfficeList(ListView):
    model = Office_Spaces


class OfficeBookingList(ListView):
    model = Office_Spaces_Booked
