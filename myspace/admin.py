from django.contrib import admin

# Import Data Tables

from .models import Office_Spaces
from .models import Office_Types
from .models import STATUS
from .models import Meeting_Rooms
from .models import Meeting_Rooms_Booked
from .models import Office_Spaces_Booked

# Register your models here.

admin.site.register(Office_Spaces)
admin.site.register(Office_Types)
admin.site.register(Office_Spaces_Booked)
