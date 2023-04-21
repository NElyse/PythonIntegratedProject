from django.db import models
from .validator import validate_national_id


class Studentinfo(models.Model):
    Regno = models.CharField(max_length=9,  unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50 )
    nid = models.CharField(max_length=16, unique=True  )
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)


class StudentMovementManagement(models.Model):
    Regno = models.CharField(max_length=9,  unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, unique=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()



