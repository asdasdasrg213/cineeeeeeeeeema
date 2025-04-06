from django.urls import path
from .views import *




urlpatterns = [
    path('', movie_list),
    path('movie_detail/<int:movie_id>/', movie_detail, name="movie_detail")
]
