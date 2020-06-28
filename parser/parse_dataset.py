import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviedb.settings")
django.setup()

from movies.models import Movie, Genre, Rating


def load_file(file):
    f = open(file, 'r').read()
    _json = json.loads(f, encoding='utf8')
    return _json


def parse_data(dset):
    for row in dset:
        m = Movie(
            name = row['name'],
            alt_name = row['alt_name'],
            year = row['year'],
            imdb_rating = row['imdb_rating'],
            rating = Rating.objects.get(name__exact=row['rating']),
        )
        m.save()
        print(m)
        for g in row['genre']:
            m.genre.add(Genre.objects.get(name__exact=g))
        m.save()
        print(m)


def main():
    dset = load_file('dataset.json')
    parse_data(dset)


if __name__ == '__main__':
    main()
