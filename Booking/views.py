from django.shortcuts import render, redirect
from .models import Pizza, Table, Booking
from Booking.booking_functions import availability
from django.db.models import Max
from django.views.generic import View
from Booking.forms import BookingForm
import datetime


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        amount = Table.objects.all().aggregate(Max('capacity'))['capacity__max']
        context = {
            'pizzas': Pizza.objects.all(),
            'now_date': str(datetime.date.today()),
            'cap_range': range(1, amount + 1)
        }
        return render(request, 'Booking/index.html', context=context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST or None)
        amount = Table.objects.all().aggregate(Max('capacity'))[
            'capacity__max']
        context = {
            'now_date': str(datetime.date.today()),
            'cap_range': range(1, amount + 1),
            'form': form
        }
        if form.is_valid():
            result = availability.try_book(form)
            if result:
                context['status'] = 'success'
                context['message'] = 'You have successfully booked a table! We will call you later to confirm your order...'
            else:
                context['status'] = 'fail'
                context['message'] = "There're no available tables matching your criteria for this period!"
        return render(request, 'Booking/form.html', context=context)
