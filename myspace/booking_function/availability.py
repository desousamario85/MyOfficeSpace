import datetime;
from myspace.models import office_spaces as office;
from myspace.models import STATUS as status;
from myspace.models import Office_Spaces_Booked as office_bookings;

def check_availability(office_id,start_datetime,end_datetime,status):
    avail_list=[]
    office_booked_list= office_bookings.objects.filter(office_id=office_id)
    for booking in office_booked_list:
        if booking.start_datetime > end_datetime and status != "Booked" or booking.end_datetime < start_datetime != "Booked":
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)