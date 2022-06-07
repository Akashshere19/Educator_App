from django.db import models
from datetime import date
# Create your models here.
class EducatorRecord(models.Model):
    FirstName=models.CharField(max_length=100)
    MiddleName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    OutDate=models.DateField()
    InDate=models.DateField()
    ClassName=models.CharField(max_length=50,unique=True)
    MobNo=models.BigIntegerField()
