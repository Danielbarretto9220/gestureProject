from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from gestureGames.camera import VideoCamera
# Create your views here.

def home(request):
    return render(request, 'Home.html')

def trex(request):
    return render(request, 'trex.html')

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
