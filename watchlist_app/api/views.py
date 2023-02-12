#type :function base views

from django.shortcuts import render
from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def movies_list(request):
    if request.method == 'GET': 
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def movies_details(request,pk):
    if request.method == 'GET':
        #IF need to get movie does not exist
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    
    if request.method == 'PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        # return status for spacific movie aafter delete it
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return the list of movie 
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
