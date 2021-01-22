import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def future_date_check(value):
    if value < datetime.date.today():
        raise ValidationError(
            _('Order date should be today or later! Value: %(val)s'),
            params={'val': value},
            code='invalid'
        )


def start_time_check(value):
    if value < datetime.datetime.strptime('18:00', '%H:%M').time():
        raise ValidationError(
            _('Order start time should be 18:00 or later! Value: %(val)s'),
            params={'val': value},
            code='invalid'
        )