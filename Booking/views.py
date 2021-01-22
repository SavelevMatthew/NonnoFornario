from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pizza, Table
from django.db.models import Max
import datetime


# Create your views here.
def index(request):
    template = loader.get_template('Booking/index.html')
    amount = Table.objects.all().aggregate(Max('capacity'))['capacity__max']
    context = {
        'pizzas': Pizza.objects.all(),
        'now_date': str(datetime.date.today()),
        'cap_range': range(1, amount + 1)
    }
    return HttpResponse(template.render(context, request=request))
