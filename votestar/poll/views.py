from django.shortcuts import render
from .models import Question, Choice

# Get Question and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'poll/index.html',context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise HTTP404('Question Doesnt Exist')
    
    return render(request, 'poll/results.html',{ 'question': question })
