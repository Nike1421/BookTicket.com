from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class movie(models.Model):
    title = models.CharField(max_length=60)
    language = models.CharField(max_length=60, choices=(
        ("English", "EN"), ("Hindi", "HI"), ("Marathi", "MR"), ("Gujarati", "GJ")))
    description = models.TextField(default='Description text')
    poster_v = models.ImageField(upload_to='poster_v/')
    poster_h = models.ImageField(upload_to='poster_h/')
    genre_1 = models.CharField(max_length=20, choices=(
        ("Action", "Action"),
        ("Horror", "Horror"),
        ("Drama", "Drama"),
        ("Comedy", "Comedy"),
        ("Biography", "Biography"),
        ("Romance", "Romance"),
        ("Thriller", "Thriller")), default="Genre_1")
    genre_2 = models.CharField(max_length=20, choices=(
        ("Action", "Action"),
        ("Horror", "Horror"),
        ("Drama", "Drama"),
        ("Comedy", "Comedy"),
        ("Biography", "Biography"),
        ("Romance", "Romance"),
        ("Thriller", "Thriller")), default="Genre_2")
    trailer = models.CharField(max_length=1000)
    duration = models.IntegerField()
    release_date = models.DateField(null=True, default='2001-12-31')
    certification = models.CharField(max_length=5, choices=(
        ("U/A", "U/A"), ("U", "U"), ("A", "A"), ("S", "S")))

    def __str__(self):
        return self.title


class theatre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class show(models.Model):
    date = models.DateField(null=True, default='2001-12-31')
    time = models.TimeField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.date}  {self.time}'


class booking(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ForeignKey(
        movie, related_name="booking_movie", null=False, default=None, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    show = models.ForeignKey(
        show, related_name="booking_show", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="booking_user",
                             null=False, default=None, on_delete=models.CASCADE)
    theatre = models.ForeignKey(
        theatre, related_name="booking_theatre", null=False, on_delete=models.CASCADE)


class seating(models.Model):
    name = models.CharField(max_length=4, null=False)
    status = models.SmallIntegerField(
        choices=((1, "Available"), (2, "Booked")), default=1)
    booking = models.ForeignKey(
        booking, related_name="seat_booking", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
