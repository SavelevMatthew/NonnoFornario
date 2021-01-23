from Booking.models import Booking, Table
from Booking.forms import BookingForm


def check_availability(table, date, time_from, time_to):
    avail_list = []
    bookings = Booking.objects.filter(table=table, date=date)
    for booking in bookings:
        if booking.time_from > time_to or booking.time_to < time_from:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)


def try_book(form: BookingForm):
    data = form.cleaned_data
    tables = Table.objects.all()
    smoking = data.get('smoking')

    # smoking filter
    if smoking != 'ANY':
        tables = tables.filter(smoking=smoking)

    # location filter
    location = data.get('location')
    if location != 'ANY':
        tables = tables.filter(location=location)

    # people filter
    people = data.get('capacity')
    if people:
        people = int(people)
        tables = tables.filter(capacity__gte=people)
    tables = tables.order_by('capacity')
    for table in tables:
        if check_availability(table, data.get('date'), data.get('time_from'), data.get('time_to')):
            b = Booking.objects.create(
                name=data.get('name'),
                phone=data.get('phone'),
                date=data.get('date'),
                time_from=data.get('time_from'),
                time_to=data.get('time_to'),
                people=people,
                table=table
            )
            b.save()
            return True
    return False
