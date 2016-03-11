from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse


# Create your views here.
# from django.http import HttpResponse

from qa.models import Question

from qa.models import Answer

from qa.forms import AskForm
from qa.forms import AnswerForm
from qa.forms import SignUpForm
from qa.forms import LoginForm



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

        if request.method == "POST":
            form = AnswerForm(request.POST)
            form._user = request.user
            if form.is_valid():
                answer = form.save()
                url = question.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AnswerForm()
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })

def ask_form(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_form.html', {
        'form': form
    })

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            form.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {
        'form': form
    })


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })