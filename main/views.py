from django.shortcuts import render
from django.apps import apps
import random


def home(request):
    movies_model = apps.get_model('movies', 'movie')

    q_set = movies_model.objects.all()
    range_set = random.sample(range(1, 38), 5)

    q_set_2 = movies_model.objects.filter(id__in=range_set)
    booking_model = apps.get_model('movies', 'booking')
    try:
        q_set_bookings = booking_model.objects.all().filter(user=request.user)
    except:
        q_set_bookings = None
    context = {'movie': q_set, 'bookings': q_set_bookings,
               'movie_range': q_set_2}
    return render(request, 'main/home.html', context)
