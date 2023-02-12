from django.urls import path,include
from watchlist_app.views import movies_list,movies_details

urlpatterns = [
    path('list/',movies_list, name='movies-list'),
    path('<int:pk>',movies_details, name='movies-details'),
]