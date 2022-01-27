from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from qa.models import Question, QuestionManager, Answer

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

@require_GET
def post_details(request, pk):
    post = get_object_or_404(Question.objects.filter(id=pk))
    answers = post.answer_set.all()
    return render(request, 'qa/post_detail.html',
                  {'post': post,
                   'answers': answers,
                  })
                  
@require_GET
def new_posts(request):
    context = extract_data(request, 'new')
    return render(request, 'qa/new_posts.html', context)

@require_GET
def popular_posts(request):
    context = extract_data(request, 'rating')
    return render(request, 'qa/new_posts.html', context)
