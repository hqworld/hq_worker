from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NaverAccount, NaverCafeList, PostList
from django.utils import timezone
from .forms import NaverAccountForm, NaverCafeListForm

# Create your views here.
def naver_work(request):
    return render(request, 'naver_work/index.html', {})

def idlist(request):
    idlist = NaverAccount.objects.all()
    query = request.GET.get('q')

    if query:
        idlist = idlist.filter(Q(naver_id__icontains=query))

    paginator = Paginator(idlist, 6)
    page = request.GET.get('page')
    idlists = paginator.get_page(page)
    context = {'idlists': idlists, 'page': page}

    return render(request, 'naver_work/idlist.html', context)

def idlist_add(request):
    if request.method == "POST":
        form = NaverAccountForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('idlist')
    else:
        form = NaverAccountForm()

    context = {'form': form}

    return render(request, 'naver_work/idlist_edit.html', context)



def cafelist(request):
    cafelist = NaverCafeList.objects.all()
    query = request.GET.get('q')
    if query:
        cafelist = cafelist.filter(
            Q(cafe_name__icontains=query)|
            Q(cafe_board__icontains=query)
            )
    paginator = Paginator(cafelist, 100)
    page = request.GET.get('page')
    cafelists = paginator.get_page(page)
    context = {'cafelists': cafelists, 'page': page}

    return render(request, 'naver_work/cafelist.html', context)

def cafelist_add(request):
    if request.method == "POST":
        form = NaverCafeListForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('cafelist')
    else:
        form = NaverCafeListForm()

    context = {'form': form}

    return render(request, 'naver_work/cafelist_edit.html', context)

def cafelist_edit(request, pk):
    cafelist = get_object_or_404(NaverCafeList, pk=pk)

    if request.method == "POST":
        form = NaverCafeListForm(request.POST, instance=cafelist)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('cafelist')
    else:
        form = NaverCafeListForm(instance=cafelist)

    context = {'form': form }

    return render(request, 'naver_work/cafelist_edit.html', context)

def postlist(request):
    postlist = PostList.objects.all()
    query = request.GET.get('q')

    if query:
        postlist = postlist.filter(Q(title__icontains=query))

    paginator = Paginator(postlist, 2)
    page = request.GET.get('page')
    postlists = paginator.get_page(page)
    context = {'postlists': postlists, 'page': page}

    return render(request, 'naver_work/postlist.html', context)

def post_detail(request, pk):
    post = get_object_or_404(PostList, pk=pk)
    context = {'post': post}
    return render(request, 'naver_work/post_detail.html', context)
