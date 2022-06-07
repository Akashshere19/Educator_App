from django.contrib import admin
from EducatorApp.models import *
# Register your models here.
@admin.register(EducatorRecord)
class EducatorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName','MiddleName','LastName', 'OutDate', 'InDate','ClassName','MobNo')
