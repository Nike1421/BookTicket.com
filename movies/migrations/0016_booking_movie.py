# Generated by Django 3.1.7 on 2021-04-22 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_remove_seating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='booking_movie', to='movies.movie'),
        ),
    ]