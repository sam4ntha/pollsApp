from django.shortcuts import redirect, render

from .models import Choice, Question
# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(request, 'polls/home.html', {"questions": questions})

def vote(request, q_id):
    question = Question.objects.get(id=q_id)

    if request.method == 'POST':
        choice = request.POST['choice']
        
        c = Choice.objects.get(id=choice)
        c.votes += 1
        c.save()

        return redirect('polls:results', q_id)
    return render(request, 'polls/question.html', { "question": question})

def results(request, q_id):
    question = Question.objects.get(id=q_id)
    return render(request, 'polls/results.html', { "question": question })