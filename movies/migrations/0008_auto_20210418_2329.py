# Generated by Django 3.1.7 on 2021-04-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_seating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seating',
            name='row',
            field=models.CharField(max_length=2),
        ),
    ]
