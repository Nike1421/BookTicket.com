from django.contrib import admin
from django import forms
from django.db import models
from .models import movie, show, theatre, seating, booking
# Register your models here.

admin.site.register(movie)
admin.site.register(show)
admin.site.register(theatre)
admin.site.register(seating)
admin.site.register(booking)

class mymodel(movie):
    formfield_overrides = {
        models.ImageField: {
            'widget': forms.ClearableFileInput(
                    attrs={
                        'multiple': True
                        }
                        )

                    
    }}