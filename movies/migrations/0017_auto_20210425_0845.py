# Generated by Django 3.1.7 on 2021-04-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_booking_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre_1',
            field=models.CharField(choices=[('Action', 'Action'), ('Horror', 'Horror'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Biography', 'Biography'), ('Romance', 'Romance'), ('Thriller', 'Thriller')], default='Genre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_2',
            field=models.CharField(choices=[('Action', 'Action'), ('Horror', 'Horror'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Biography', 'Biography'), ('Romance', 'Romance'), ('Thriller', 'Thriller')], default='Genre_2', max_length=20),
        ),
    ]
