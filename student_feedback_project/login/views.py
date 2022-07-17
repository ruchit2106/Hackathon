from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html');

def registerParticipant(request):
    return render(request,'registerParticipant.html');

#def verifyLogin(request):
#    email=request.POST['uemail'];
#    password=request.POST['upassword'];
#
#   if()