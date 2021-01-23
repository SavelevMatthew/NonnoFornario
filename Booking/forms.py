from django import forms
from django.utils.translation import gettext as _
from phonenumber_field.formfields import PhoneNumberField
from Booking.booking_functions import choices
from Booking.models import location_choice, smoking_choice
import datetime


class BookingForm(forms.Form):
    name = forms.CharField(max_length=32)
    phone = PhoneNumberField()
    date = forms.DateField(input_formats=['%d.%m.%Y', '%Y-%m-%d'])

    time_from = forms.TimeField()
    time_to = forms.TimeField()

    capacity = forms.ChoiceField(choices=(('1', '1'),))

    l_choices = location_choice + (('ANY', 'Any'), )
    location = forms.ChoiceField(choices=l_choices)

    s_choices = smoking_choice + (('ANY', 'Any'),)
    smoking = forms.ChoiceField(choices=s_choices, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['capacity'].choices = choices.get_proper_table_choices()

    def clean_date(self):
        data = self.cleaned_data.get('date')
        if data < datetime.date.today():
            raise forms.ValidationError(
                _('Date should be today or later'),
                code='invalid'
            )
        return data

    def clean_time_from(self):
        t = self.cleaned_data.get('time_from')
        if t < datetime.datetime.strptime('18:00', '%H:%M').time():
            raise forms.ValidationError(
                _('You can book only from 18:00'),
                code='invalid'
            )
        return t

    def clean_time_to(self):
        t_t = self.cleaned_data.get('time_to')
        if t_t < datetime.datetime.strptime('18:00', '%H:%M').time():
            raise forms.ValidationError(
                _('End of booking cannot be less than 18:00'),
                code='invalid'
            )
        t_f = self.cleaned_data.get('time_from')
        if t_f >= t_t:
            raise forms.ValidationError(
                _('Start time of booking should be less than end time'),
                code='invalid'
            )
        return t_t

    # TODO: make add to base
    # TODO: make preloader
    # TODO: make readme
    # TODO: SEND
