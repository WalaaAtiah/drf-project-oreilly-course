from django.urls import path,include
from .views import movies_details,movies_list

# views is class type 
urlpatterns = [
    path('list/',movies_list.as_view(), name='movies-list'),
    path('<int:pk>',movies_details.as_view(), name='movies-details'),
]



# views is function type 
# urlpatterns = [
#     path('list/',movies_list, name='movies-list'),
#     path('<int:pk>',movies_details, name='movies-details'),
# ]