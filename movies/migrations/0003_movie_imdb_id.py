# Generated by Django 3.1.4 on 2021-01-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_watched'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]