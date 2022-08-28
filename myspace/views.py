from django.shortcuts import render
from django.views.generic import ListView
from .models import Office_Spaces
from .models import Office_Spaces_Booked

# Create your views here.

class OfficeList(ListView):
    """
    List of Office Spaces
    """
    model = Office_Spaces
    template_name = 'office_list.html'

    
class OfficeBookedList(ListView):
    """
    List of Office Spaces
    """
    model = Office_Spaces_Booked
    template_name = 'office_bookings.html'

