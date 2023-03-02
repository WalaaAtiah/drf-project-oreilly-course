
from django.shortcuts import render
from watchlist_app.models import Movie,WatchList,StreamPlatform,Review
from .serializers import WatchSerializer,StreamPlatSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view #for function type
from rest_framework import status,generics,mixins
from rest_framework.views import APIView #for class type
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
################################## for Review module   Using  generic concreate view class ###########################################

class Review_list(generics.ListCreateAPIView):
    '''
    this class to see all the review
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class Review_Detail(generics.RetrieveUpdateDestroyAPIView):
    '''
    this class to see specific review
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
 
    
class MovieReview_list(generics.ListCreateAPIView):
    '''
    this class to see all the review in particular movie (watch)
    '''
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        # print(pk)
        return Review.objects.filter(watchlist=pk)
    
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        print(pk)
        movie=WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)
    
class MovieReview_Create(generics.CreateAPIView):
    '''
    this class to craet a review in particular movie (watch)
    '''
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        print(pk)
        movie=WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)

    
################################## for Review module   Using mixins ###########################################

# class Review_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class Review_Detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

############################################# for StreamPlatform module ###########################################
# use viewset and router to creat stream palt
class StreamPlatView(viewsets.ModelViewSet):
   
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatSerializer
    
    


# use viewset and router to creat stream palt
# class StreamPlatView(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatSerializer(watchlist)
#         return Response(serializer.data)
    
    
    
#type :class base views +serializers.serializer

# class StreamPlat_list(APIView):
#     def get(self, request):
#         stream=StreamPlatform.objects.all()
#         serializer=StreamPlatSerializer(stream,many=True,context={'request': request} ) 
#         # serializer=StreamPlatSerializer(stream,many=True ,context={'request': request}) #for HyperlinkedRelatedField (serializer relation) and HyperlinkedModelSerializer class
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=StreamPlatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
    
# class StreamPlat_Detail(APIView):
#     def get(self,request,pk):
#         try:
#             stream=StreamPlatform.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=StreamPlatSerializer(stream,context={'request': request})   #for HyperlinkedRelatedField (serializer relation) and HyperlinkedModelSerializer class
#         # serializer=StreamPlatSerializer(stream)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         stream=StreamPlatform.objects.get(pk=pk)
#         serializer=StreamPlatSerializer(stream,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self,request,pk):   
#         stream=StreamPlatform.objects.get(pk=pk)
#         stream.delete()
#         # return status for spacific movie aafter delete it
#         return Response(status=status.HTTP_204_NO_CONTENT)
#         # return the list of movie 
#         streams=Movie.objects.all()
#         serializer=StreamPlatSerializer(movies,many=True)
#         return Response(serializer.data)




############################################# for Watchlist module  ###########################################

#type :class base views +serializers.serializer

class Watch_list(APIView):
    def get(self, request):
        movies=WatchList.objects.all()
        serializer=WatchSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
class Watch_details(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):   
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        # return status for spacific movie aafter delete it
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return the list of movie 
        movies=Movie.objects.all()
        serializer=WatchSerializer(movies,many=True)
        return Response(serializer.data)





#*******************************************************************************************************************
################################################## for movie module ######################################

#type :class base views +serializers.ModelSerializer

# class movies_list(APIView):
#     def get(self, request):
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
    
# class movies_details(APIView):
#     def get(self,request,pk):
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self,request,pk):   
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         # return status for spacific movie aafter delete it
#         return Response(status=status.HTTP_204_NO_CONTENT)
#         # return the list of movie 
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)



#type :function base views +serializers.serializer

# @api_view(['GET','POST'])
# def movies_list(request):
#     if request.method == 'GET': 
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# @api_view(['GET','PUT','DELETE'])
# def movies_details(request,pk):
#     if request.method == 'GET':
#         #IF need to get movie does not exist
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
    
#     if request.method == 'PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         # return status for spacific movie aafter delete it
#         return Response(status=status.HTTP_204_NO_CONTENT)
#         # return the list of movie 
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
