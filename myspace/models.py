from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Open"), (1, "Booked"), (2, "Cancelled"))

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name

class Office_Spaces(models.Model):
    office_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,related_name="Category"
        )

    def __str__(self):
        return self.office_name

class Meeting_Rooms(models.Model):
    meeting_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.meeting_name


class Meeting_Rooms_Booked(models.Model): 
    meeting_id = models.ForeignKey(Meeting_Rooms,on_delete=models.SET_NULL,null=True)
    category_id = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meeting_id

    class Meta:
        ordering = ['created_on']


class Office_Spaces_Booked(models.Model):
    Office_Space_id = models.ForeignKey(Office_Spaces,on_delete=models.SET_NULL,null=True)
    category_id = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()


    def __str__(self):
        return self.Office_Space_id

    class Meta:
        ordering = ['created_on']
