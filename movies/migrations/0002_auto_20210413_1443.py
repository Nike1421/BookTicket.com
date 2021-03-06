# Generated by Django 3.1.7 on 2021-04-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='certification',
            field=models.CharField(choices=[('U/A', 'U/A'), ('U', 'U'), ('A', 'A'), ('S', 'S')], max_length=5),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('English', 'EN'), ('Hindi', 'HI'), ('Marathi', 'MR'), ('Gujarati', 'GJ')], max_length=60),
        ),
    ]
