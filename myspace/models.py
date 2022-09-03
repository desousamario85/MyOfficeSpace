from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from cloudinary.models import CloudinaryField

from django.utils import timezone

# Create your models here.

STATUS = ((0, "Open"), (1, "Booked"), (2, "Cancelled"))

class Office_Types(models.Model):
    office_type = models.CharField(max_length=20,default="Small")
    
    def __str__(self):
        return self.office_type

class Office_Spaces(models.Model):
    office_name = models.CharField(max_length=50)
    office_type = models.ForeignKey(
        Office_Types,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.office_name

class Meeting_Rooms(models.Model):
    meeting_name = models.CharField(max_length=50)
    office_type = models.ForeignKey(
        Office_Types,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.meeting_name


class Meeting_Rooms_Booked(models.Model): 
    meeting_id = models.ForeignKey(Meeting_Rooms,on_delete=models.SET_NULL,null=True)
    office_type = models.ForeignKey(Office_Types,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meeting_id

    class Meta:
        ordering = ['created_on']


class Office_Spaces_Booked(models.Model):
    Office_Space_id = models.ForeignKey(Office_Spaces,on_delete=models.SET_NULL,null=True)
    office_type = models.ForeignKey(Office_Types,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()  

    def __str__(self):
        return f'{self.Office_Space_id} was booked for {self.start_datetime} until {self.end_datetime}'

    class Meta:
        ordering = ['created_on']