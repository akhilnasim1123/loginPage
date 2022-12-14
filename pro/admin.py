from django.contrib import admin

from pro.models import studentData
from pro.models import Teacher

# Register your models here.
admin.site.register(studentData),
admin.site.register(Teacher)