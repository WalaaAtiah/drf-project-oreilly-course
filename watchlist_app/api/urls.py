from django.urls import path,include
from .views import movies_details,movies_list

urlpatterns = [
    path('list/',movies_list, name='movies-list'),
    path('<int:pk>',movies_details, name='movies-details'),
]