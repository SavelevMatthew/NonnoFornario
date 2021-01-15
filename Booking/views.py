from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pizza


# Create your views here.
def index(request):
    template = loader.get_template('Booking/index.html')
    context = {
        'pizzas': Pizza.objects.all()
    }
    return HttpResponse(template.render(context, request=request))
