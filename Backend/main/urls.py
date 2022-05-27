from django.urls import path
from .views import *

urlpatterns = [

    path("users/", UserTechAPIView.as_view(), name='users'),
    path("users/<int:pk>/", UserTechAPIView.as_view(), name='usersPk'),

    path("devices/", DevicesAPIView.as_view(), name='devices'),
    path("devices/<int:pk>/", DevicesAPIView.as_view(), name='devicesPk'),
   
    path("comments/", CommentsAPIView.as_view(), name='comments'),
    path("comments/<int:pk>/", CommentsAPIView.as_view(), name='commentsPk'),

]