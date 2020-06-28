from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = (
            'name',
            'alt_name',
            'year',
            'imdb_rating',
            'rating',
            'genre',
        )
