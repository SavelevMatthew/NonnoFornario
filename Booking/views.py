from django.shortcuts import render, redirect
from .models import Pizza, Table
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
        form = BookingForm(request.POST)
        if form.is_valid():
            return redirect('home')
        amount = Table.objects.all().aggregate(Max('capacity'))[
            'capacity__max']
        context = {
            'pizzas': Pizza.objects.all(),
            'now_date': str(datetime.date.today()),
            'cap_range': range(1, amount + 1),
            'form': form
        }
        return render(request, 'Booking/index.html', context=context)
