from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('trex/', views.trex, name='trex'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('video_stream', views.video_stream, name='video_stream'),
]
