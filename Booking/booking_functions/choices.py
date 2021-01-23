from django.db.models import Max
from Booking.models import Table


def get_proper_table_choices():
    amount = Table.objects.all().aggregate(Max('capacity'))['capacity__max']
    choices = []
    for i in range(1, amount + 1):
        choices.append((str(i), str(i)))
    return tuple(choices)
