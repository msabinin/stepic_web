from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question, QuestionManager

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html',
                  {'post': post,}
                  )

def new_posts(request):
    posts = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    print(posts.values_list(), paginator.baseurl)
    return render(request,  'qa/new_posts.html', {
        'posts': page.object_list,
        'paginator': paginator,  page: page,
        })

def popular_posts(request):
    posts = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    print(posts.values_list(), paginator.baseurl)
    return render(request,  'qa/new_posts.html', {
        'posts': page.object_list,                                                                                              'paginator': paginator,  page: page,
        })
