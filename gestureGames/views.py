from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from gestureGames.camera import VideoCamera
from gestureGames.camera2 import VideoCamera2
#from gestureGames.camera3 import VideoCamera3
from gestureGames.camera3 import Game
from gestureGames.camera4 import VideoCamera4

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

# Hand Criket 
def hc(request):
    return render(request, 'hc.html')

def gen3(camera3):
    #obj = camera3.game_main()
    camera3.th1.start()
    flag = 0
    camera3.th2.start()
    while flag ==0:
        flag = camera3.queue.isEmpty()
        if not flag:
            print("Message from gen3: In Flag")
            frame3 = camera3.queue.dequeue()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame3 + b'\r\n\r\n')
    #obj.th1.join()

def video_stream3(request):
    return StreamingHttpResponse(gen3(Game()),
                    content_type='multipart/x-mixed-replace; boundary=frame')


# Rock Paper Sicssors
def rps(request):
    return render(request, 'rps.html')

def gen4(camera4):
    while True:
        frame = camera4.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_stream4(request):
    return StreamingHttpResponse(gen4(VideoCamera4()),
                    content_type='multipart/x-mixed-replace; boundary=frame')