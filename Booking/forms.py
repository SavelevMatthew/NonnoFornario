from django import forms
from phonenumber_field.formfields import PhoneNumberField


class BookingForm(forms.Form):
    name = forms.CharField(max_length=32)
    phone = PhoneNumberField()
    date = forms.DateField()

    time_from = forms.TimeField()
    time_to = forms.TimeField()

    capacity = forms.ChoiceField()
    location = forms.ChoiceField()
    smoking = forms.ChoiceField(widget=forms.RadioSelect)



