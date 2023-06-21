from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)


def detail(request):
    pass


def vote(request):
    pass


def results(request):
    pass
