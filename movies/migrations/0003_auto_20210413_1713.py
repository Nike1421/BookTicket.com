# Generated by Django 3.1.7 on 2021-04-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210413_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_h',
            field=models.ImageField(upload_to='poster_h/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_v',
            field=models.ImageField(upload_to='poster_v/'),
        ),
    ]
