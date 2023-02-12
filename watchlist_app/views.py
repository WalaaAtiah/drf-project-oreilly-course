from django.shortcuts import render
from django.http import JsonResponse
from watchlist_app.models import Movie

def movies_list(request):
    movies=Movie.objects.all()
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data)

def movies_details(request,pk):
    movies=Movie.objects.get(pk=pk)
    data={
        'name':movies.name,
        'description':movies.description,
        'active':movies.active
    }
    return JsonResponse(data)

# Create your views here.
