from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Booking.booking_functions.validators import future_date_check, start_time_check

smoking_choice = (
    ('YES', 'Smoking table'),
    ('NO', 'No smoking table'),
)
location_choice = (
    ('WND', 'Near to window'),
    ('CEN', 'In center of restaurant'),
    ('COR', 'Corner of restaurant')
)
status_choice = (
    ('SUBM', 'Submitted order'),
    ('CONF', 'Confirmed order'),
    ('CANC', 'Cancelled order')
)


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=64, help_text='Pizza caption')

    proteins = models.DecimalField(max_digits=3, decimal_places=1, help_text='Amount of proteins in 100g of a product')
    fats = models.DecimalField(max_digits=3, decimal_places=1, help_text='Amount of fats in 100g of a product')
    carbohydrates = models.DecimalField(max_digits=3, decimal_places=1, help_text='Amount of carbohydrates in 100g of a product')
    calories = models.DecimalField(max_digits=3, decimal_places=0, help_text='Amount of calories in 100g of a product')

    composition = models.TextField(help_text='What this product contains')
    
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                help_text='price in $')

    image = models.ImageField(upload_to='Booking/menu/')

    def __str__(self):
        return self.name


class Table(models.Model):
    smoking = models.CharField(max_length=4, choices=smoking_choice, help_text='Is smoking allowed?')
    location = models.CharField(max_length=3, choices=location_choice, help_text='Where is the table?')
    capacity = models.IntegerField(help_text='How much persons can be placed here?')

    def __str__(self):
        return f'Table {self.id} for {self.capacity} people. Smoking: {self.smoking}, location: {self.location}'


class Booking(models.Model):
    name = models.CharField(max_length=32, help_text='Client name')
    phone = PhoneNumberField(null=False, blank=False, help_text='Contact phone')
    
    date = models.DateField(help_text='Day of the order',
                            validators=[future_date_check])
    time_from = models.TimeField(help_text='Reservation start (min-val: 18:00)', validators=[start_time_check])
    time_to = models.TimeField(help_text='Reservation end (max-val: 23:59)', validators=[start_time_check])

    people = models.IntegerField(help_text='For how much persons?')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    status = models.CharField(max_length=4, choices=status_choice,
                              default=status_choice[0][0])

    def __str__(self):
        return f'[{self.status}] {self.name}, {self.phone} | {self.people} peop. | {self.date} | from {self.time_to} to {self.time_to}'
