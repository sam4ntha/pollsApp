from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Question
# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(request, 'polls/home.html', {"questions": questions})

def vote(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if request.method == 'POST':
        try:
            choice = request.POST['choice']
            c = Choice.objects.get(id=choice)
            c.votes += 1
            c.save()
            return redirect('polls:results', q_id)
        except (KeyError):
            return render(request, 'polls/question.html', { "question": question, "error_message": "¡Debes seleccionar una opción!"})
        
    return render(request, 'polls/question.html', { "question": question})

def results(request, q_id):
    try:
        question = Question.objects.get(id=q_id)
    except Question.DoesNotExist:
        raise Http404("¡No existe la encuesta!")
    return render(request, 'polls/results.html', { "question": question })