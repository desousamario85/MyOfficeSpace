from django.shortcuts import render, HttpResponse
from django.views.generic import FormView
from django.views import generic, View
from .models import Office_Spaces
from .models import Office_Spaces_Booked
from .forms import AvailabilityForm
from myspace.booking_function.availability import check_availability

# Create your views here.

class OfficeList(generic.ListView):
    """
    List of Office Spaces
    """
    model = Office_Spaces
    queryset = Office_Spaces.objects.order_by("-office_name")
    template_name = 'index.html'
    paginate_by = 6
    
class OfficeBookedList(generic.ListView):
    """
    List of Office Spaces
    """
    model = Office_Spaces_Booked
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Office_Spaces_Booked.objects.all()
            return booking_list
        else:
            booking_list = Office_Spaces_Booked.objects.filter(user=self.request.user)
    template_name = 'office_bookings.html'
    paginate_by = 10

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability.html'

    def form_valid(self, form):
        data = form.cleaned_data
        office_list = Office_Spaces.objects
        available_offices = []

        for office in office_list:
            if check_availability(office_name, data['start_datetime'], 
                                  data['end_datetime']):
                available_offices.append(office)
        if len(available_offices) > 0:
            office = available_offices[0]
            booking = Office_Spaces_Booked.objects.create(
                user = request.user,
                Office_Space_id = office,
                start_datetime=data['start_datetime'],
                end_datetime=data['end_datetime'],
                status="Booked"

            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('No available offices for selected category.'
                                'Please try another category')


