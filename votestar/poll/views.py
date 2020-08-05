from django.shortcuts import render
from .models import Question, Choice

# Get Question and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questionn_list': latest_question_list
    }
    return render(request,'poll/index.html',context)


