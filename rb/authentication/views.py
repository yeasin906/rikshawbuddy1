from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello I am working")

def signup(request):
    return render("Hello I am working")