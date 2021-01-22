from django.contrib import admin
from .models import Pizza, Table, Booking

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Table)
admin.site.register(Booking)
