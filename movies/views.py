from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from .forms import MovieForm
from django.views.generic.detail import DetailView
from .models import movie, booking, theatre, show, seating
from django.contrib.auth.decorators import login_required
import json

base_seat_state = {
    'A1': 'vacant',
    'A2': 'vacant',
    'A3': 'vacant',
    'A4': 'vacant',
    'A5': 'vacant',
    'B1': 'vacant',
    'B2': 'vacant',
    'B3': 'vacant',
    'B4': 'vacant',
    'B5': 'vacant',
    'C1': 'vacant',
    'C2': 'vacant',
    'C3': 'vacant',
    'C4': 'vacant',
    'C5': 'vacant',
    'D1': 'vacant',
    'D2': 'vacant',
    'D3': 'vacant',
    'D4': 'vacant',
    'D5': 'vacant',
    'E1': 'vacant',
    'E2': 'vacant',
    'E3': 'vacant',
    'E4': 'vacant',
    'E5': 'vacant',
    'F1': 'vacant',
    'F2': 'vacant',
    'F3': 'vacant',
    'F4': 'vacant',
    'F5': 'vacant',
    'G1': 'vacant',
    'G2': 'vacant',
    'G3': 'vacant',
    'G4': 'vacant',
    'G5': 'vacant',
    'H1': 'vacant',
    'H2': 'vacant',
    'H3': 'vacant',
    'H4': 'vacant',
    'H5': 'vacant',
}


def upload_m(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MovieForm()
    return render(request, 'movies/movies_upload.html', {'form': form})


class dash(DetailView):
    model = movie


def get_seats(sel_movie, sel_theatre, sel_show):
    ref_bookings = booking.objects.filter(
        movie=sel_movie, theatre=sel_theatre, show=sel_show)
    ref_seats = seating.objects.filter(booking__in=ref_bookings).values()
    seat_state = base_seat_state.copy()
    for i in ref_seats:
        seat_state[i['name']] = 'taken'
    return seat_state


@login_required(login_url='accounts-login')
def book(request, pk):
    if (request.method == 'POST'):
        data = json.load(request)
        theatre_id = data['theatreId']
        show_id = data['showId']
        movie_id = data['movieId']
        sel_theatre = theatre.objects.get(pk=theatre_id)
        sel_show = show.objects.get(pk=show_id)
        sel_movie = movie.objects.get(pk=movie_id)
        if 'refreshSeats' in data:
            seats = get_seats(sel_movie, sel_theatre, sel_show)
            return JsonResponse(seats)
        else:
            try:
                new_booking = booking.objects.create(
                    user=request.user,
                    show=sel_show,
                    theatre=sel_theatre,
                    movie=sel_movie,
                )

                seats_list = []

                for seat_name, state in data['seatState'].items():
                    if state == 'selected':
                        seats_list.append(seat_name)
                        seating.objects.create(
                            name=seat_name,
                            status=2,
                            booking=new_booking
                        )

                if len(seats_list) == 1:
                    message = seats_list[0]
                else:
                    message = ''
                    for seat in seats_list[:-2]:
                        message += seat + ', '

                    message += seats_list[-2] + ' and '
                    message += seats_list[-1]

                message = 'You have selected seats: ' + message
                message += f' for {sel_movie} at {sel_theatre} on {sel_show}'

                send_mail(
                        f'Receipt for your booking of {sel_movie}',
                        message,
                        '123moviebookings@gmail.com',
                        [request.user.email]
                )

                return JsonResponse({
                    'success': True
                })
            except:
                return JsonResponse({
                    'success': False
                })
    else:
        all_theatres = theatre.objects.values().order_by('id')
        all_shows = show.objects.values().order_by('id')
        all_movies = movie.objects.get(pk=pk)
        return render(request,  'movies/movie_booking.html', {
            'pk': pk,
            'theatres': all_theatres,
            'shows': all_shows,
            'movies': all_movies
        })
