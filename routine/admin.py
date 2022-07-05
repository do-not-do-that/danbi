from django.contrib import admin
from .models import RoutineResult, Routine, RoutineDay
# Register your models here.

admin.site.register(Routine)
admin.site.register(RoutineResult)
admin.site.register(RoutineDay)