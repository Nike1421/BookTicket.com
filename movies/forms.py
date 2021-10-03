from django import forms
from .models import movie, show, theatre, booking, seating


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['title', 'language', 'description', 'poster_v',
                  'poster_h', 'trailer', 'duration', 'release_date', 'certification']
        widgets = {
            'release_date': DateInput(),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['name', 'show', 'theatre']


class SeatingForm(forms.ModelForm):
    class Meta:
        model = seating
        exclude = ['row', 'column', 'status', 'user']
