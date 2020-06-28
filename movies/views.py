from django.shortcuts import render, redirect
from django.http import HttpResponse
# import operator
from django.db.models import Q
from datetime import datetime
# from django.views import generic
# from django.http import HttpResponseRedirect
from django.conf import settings

from .forms import MovieForm
from .models import Movie, Genre, Rating


# Create your views here.


def movies(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return HttpResponse("Submitted!")
    else:
        form = MovieForm()
    return render(request, 'movies/movies.html', {'form': form})


def index(request):
    if (request.method == 'POST') and (request.POST.get('q') != ''):
        query = request.POST.get('q').strip()
        result = Movie.objects.filter(
            Q(name__icontains=query) | Q(alt_name__icontains=query)
        )
        context = {
            'header': "Search results",
            'movies': result,
            'imdb_prefix': settings.IMDB_PREFIX,
        }
    else:
        context = {
            'header': "Last 100 records",
            'movies': Movie.objects.all().order_by('-id')[:100],
            'count': Movie.objects.all().count(),
            'imdb_prefix': settings.IMDB_PREFIX,
        }
    return render(request, 'movies/index.html', context)


def filter(request):
    genres = []
    ratings = []
    for genre in Genre.objects.all():
        genres.append(genre)
    for rating in Rating.objects.all():
        ratings.append(rating)

    ratings.insert(0, '----')
    context = {
        'genres': genres,
        'ratings': ratings,
    }

    if request.method == 'POST':
        qrating = request.POST.get('rating')
        qgenres = ''
        for i in request.POST.lists():  # Used for multiple choice filed
            if i[0] == 'genres':
                qgenres = i[1]

        if qrating == '----' and qgenres == '':
            return HttpResponse("Select at least a rating or a genre")
        result = Movie.objects.all()
        if qrating != '----':
            result = result.filter(rating__name__exact=qrating)
        if qgenres != '':
            for genre in qgenres:
                result = result.filter(genre__name__exact=genre)

        result = result.order_by('-year')

        context['movies'] = result
        context['count'] = result.count()

    return render(request, 'movies/filter.html', context)


def about(request):
    count = Movie.objects.all().count()
    start_date = datetime.strptime('2011-01-01', '%Y-%m-%d')
    interval = datetime.now() - start_date
    average = interval.days / count
    context = {
        'count': count,
        'average': average,
    }
    return render(request, 'movies/about.html', context)


def bye(request):
    return render(request, 'movies/bye.html')


def to_root(request):
    return redirect('/index')
