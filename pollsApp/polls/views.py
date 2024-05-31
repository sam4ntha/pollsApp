from io import BytesIO
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import matplotlib.pyplot as plt

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

def results_chart(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    choices = question.choice_set.all()
    labels = [c.choice_text for c in choices]
    sizes = [c.votes for c in choices]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para que el gráfico sea un círculo

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type='image/png')
