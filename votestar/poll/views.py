from django.shortcuts import render
from .models import Question, Choice

# Get Question and display them

def index(request):
    return render(request,'polls/index.html')


