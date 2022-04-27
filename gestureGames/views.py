from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from gestureGames.camera import VideoCamera
from gestureProject.gestureGames.camera2 import VideoCamera2
# Create your views here.

def home(request):
    return render(request, 'Home.html')


# TReX
def trex(request):
    return render(request, 'trex.html')

def gen2(camera2):
    while True:
        frame2 = camera2.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')

def video_stream2(request):
    return StreamingHttpResponse(gen2(VideoCamera2()),
                content_type = 'multipart/x-mixed-replace; boundary=frame')


# Tic Tac Toe
def tictactoe(request):
    return render(request, 'tictactoe.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def video_stream(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

