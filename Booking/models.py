from django.db import models


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
