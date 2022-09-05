from django.shortcuts import render, HttpResponse
from django.views.generic import FormView
from django.views import generic, View
from .models import Office_Spaces, Office_Types
from .models import Office_Spaces_Booked
from .forms import AvailabilityForm, ContactForm
from myspace.booking_function.availability import check_availability
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static
# Create your views here.

class OfficeList(generic.ListView):
    """
    List of Office Spaces
    """
    model = Office_Spaces
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
        office_list = Office_Spaces.objects.filter(category_id=data['category_name'])
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



class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


def error_404_view(request, exception):
    return render(request, '404.html')