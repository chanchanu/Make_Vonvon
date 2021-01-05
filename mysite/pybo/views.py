from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
#from .forms import QuestionForm, AnswerForm
from django.utils import timezone
from .models import *
# Create your views here.

def main(request):
    quiz = Quiz.objects.all()
    quiz_list = {'quiz': quiz}
    return render(request, 'main.html', quiz_list)

def quiz1(request,title):
    det = D.objects.filter(tit = title, id = 1)
    det_list = {'det': det}
    return render(request, 'quiz1.html', det_list)

def render_quiz(request, det, d):
    dd = get_object_or_404(D,id=det)
    det= int(det)+1
    d2 = get_object_or_404(D,id=det)
    return render(request, 'quiz1-1.html', {'det': dd, 'det2':d2})