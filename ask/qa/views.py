from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render


# Create your views here.
# from django.http import HttpResponse

from qa.models import Question

from qa.models import Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def homepage(request, *args, **kwargs):
    questions = Question.objects.all().order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'homepage.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def popular(request, *args, **kwargs):
    questions = Question.objects.all().order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def question(request, id):
    try:
        question = Question.objects.get(id=id)
        answers = question.answer_set.all()
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })
