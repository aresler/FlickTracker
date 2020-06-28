import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviedb.settings")
django.setup()

from movies.models import Genre

list = ['Action', 'Drama', 'Comedy', 'Thriller', 'Adventure', 'Sci-Fi', 'Fantasy', 'Horror', 'Romance', 'Crime', 'Mystery', 'Western', 'Biography', 'Sport', 'War', 'Family', 'History', 'Music', 'Documentary', 'Martial arts', 'Musical', 'Animation']

for item in list:
    Genre.objects.create(name=item)