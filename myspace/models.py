from django.db import models

# Create your models here.

class category(models.Model):
    ID = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return (self.category_name)

class office_spaces(models.Model):
    ID = models.IntegerField(primary_key=True)
    office_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        category,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return (self.office_name)

class status(models.Model):
    ID = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=10)
    def __str__(self):
        return (self.status_name)

class meeting_rooms(models.Model):
    ID = models.IntegerField(primary_key=True)
    meeting_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        category,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return (self.meeting_name)
