from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


# def index(request):
#     latest_questions_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_questions_list': latest_questions_list
#     }
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Return five last published"""
        return Question.objects.order_by('-pub_date')[:]


# def detail(request, question_id):
#     question = Question.objects.get(id=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You selected no choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
