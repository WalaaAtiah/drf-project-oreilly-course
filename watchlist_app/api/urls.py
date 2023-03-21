from django.urls import path,include
from .views import Watch_list,Watch_details,Review_list,Review_Detail,MovieReview_list,MovieReview_Create,StreamPlatView
from rest_framework.routers import DefaultRouter


############################################# for router ###########################################

router = DefaultRouter()
router.register(r'stream', StreamPlatView, basename='streamplatform')


############################################# for normal urls ###########################################
urlpatterns = [
    path('movie/',Watch_list.as_view(), name='Watch-list'),
    path('movie/<int:pk>/',Watch_details.as_view(), name='Watch-details'),
    
    path('',include(router.urls)),  #for stream 
    
    path('review/',Review_list.as_view(), name='Review_list'),
    path('review/<int:pk>/',Review_Detail.as_view(), name='Review_Detail'),
    
    path('movie/<int:pk>/review/',MovieReview_list.as_view(), name='Movie_Review_list'),
    path('movie/<int:pk>/create_review/',MovieReview_Create.as_view(), name='Movie_Review_create'),
     
     
    # path('stream/',StreamPlat_list.as_view(), name='StreamPlat-list'),
    # path('stream/<int:pk>',StreamPlat_Detail.as_view(), name='StreamPlat_Detail'),
    
]





##################################################for movie module ######################################
# views is class type 
# urlpatterns = [
#     path('list/',movies_list.as_view(), name='movies-list'),
#     path('<int:pk>',movies_details.as_view(), name='movies-details'),
# ]



# views is function type 
# urlpatterns = [
#     path('list/',movies_list, name='movies-list'),
#     path('<int:pk>',movies_details, name='movies-details'),
# ]