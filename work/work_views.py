from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Task, Account, PostList
from django.utils import timezone
from .forms import TaskForm, AccountForm, PostListForm



def work(request):
    return render(request, 'work/index.html', {})


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            account = form.cleaned_data['account']
            
            #이곳에 Account 모델의 id, pw 등의 데이터를 가져오려고 합니다.
            #id = ''
            #pw = ''
            #nick = ''

            post.save()
            form.save_m2m()
            id = post.account
            print(id)
            idlist = Account.objects.get(pk='1')
            print(idlist)
            return redirect('task')
    else:
        form = TaskForm()

    context = {'form': form}


    return render(request, 'naver_work/task.html', context)

def idlist(request):
    idlist = Account.objects.all()
    query = request.GET.get('q')

    if query:
        idlist = idlist.filter(Q(id__icontains=query))

    paginator = Paginator(idlist, 2)
    page = request.GET.get('page')
    idlists = paginator.get_page(page)
    context = {'idlists': idlists, 'page': page}

    return render(request, 'work/idlist.html', context)


def postlist(request, ):
    postlist = PostList.objects.all()
    query = request.GET.get('q')

    if query:
        postlist = postlist.filter(Q(title__icontains=query))

    paginator = Paginator(postlist, 100)
    page = request.GET.get('page')
    postlists = paginator.get_page(page)
    context = {'postlists': postlists, 'page': page}

    return render(request, 'work/postlist.html', context)

def post_add(request):
    if request.method == "POST":
        form = PostListForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m() #taggit 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostListForm()

    context = {'form': form}

    return render(request, 'work/post_edit.html', context)

def post_detail(request, pk):
    post = get_object_or_404(PostList, pk=pk)
    context = {'post': post}

    return render(request, 'work/post_detail.html', context)

def post_edit(request, pk):
    post = get_object_or_404(PostList, pk=pk)

    if request.method == "POST":
        form = PostListForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m() #taggit 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostListForm(instance=post)

    context = {'form': form }

    return render(request, 'work/post_edit.html', context)
