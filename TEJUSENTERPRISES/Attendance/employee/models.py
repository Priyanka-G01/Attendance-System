from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=25)
    eid =  models.IntegerField()
    eaadhar = models.IntegerField()
    eage = models.IntegerField()
    econtact = models.IntegerField()

class Attendance(models.Model):
    name = models.CharField(max_length=252)
    hours = models.FloatField()
    OT = models.FloatField()

