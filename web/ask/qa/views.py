from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from qa.models import Question, QuestionManager, Answer
from qa.forms import *

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def extract_data(request, data_sort_type):
    if data_sort_type == 'new':
        posts = Question.c_objects.new()
        baseurl = '/?page='
    elif data_sort_type == 'rating':
        posts = Question.c_objects.popular()
        baseurl = '/popular/?page='
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = baseurl
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
 
    context = {
               'posts': page.object_list,
               'paginator': paginator,  
               'page': page,
              }
    return context

@login_required(login_url='/login/')
def post_details(request, pk):
    post = get_object_or_404(Question.objects.filter(id=pk))
    answers = post.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': post.id})    

    return render(request, 'qa/post_detail.html',
                  {'post': post,
                   'answers': answers,
                   'form': form,
                  })

@require_GET
def new_posts(request):
    context = extract_data(request, 'new')
    return render(request, 'qa/new_posts.html', context)

@require_GET
def popular_posts(request):
    context = extract_data(request, 'rating')
    return render(request, 'qa/new_posts.html', context)

@login_required(login_url='/login/')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = '/question/{}/'.format(post.id)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/post_add.html', 
                   {'form': form,
                    'user': request.user,
                     'session': request.session, 
                   })

def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})

def userSignUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})
