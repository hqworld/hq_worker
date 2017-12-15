from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NaverTask, NaverAccount, NaverCafeList, PostList
from django.utils import timezone
from .forms import NaverTaskForm, NaverAccountForm, NaverCafeListForm, PostListForm
from selenium import webdriver
import time, requests
from selenium.webdriver.common.keys import Keys



# Create your views here.
def test(request, pk): #수정 시 html에서 태그 추가,삭제가능하도록 해야함.test.html tags연결
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

    return render(request, 'naver_work/test.html', context)

def naver_work(request):

    return render(request, 'naver_work/index.html', {})


def task(request): #실제 글 작업태스크(추가로 작업대기시간 등 디테일 추가)
    idlists = NaverAccount.objects.all()
    cafelists = NaverCafeList.objects.all()
    postlists = PostList.objects.all()

    if request.method == 'POST':
        
        form = NaverTaskForm(request.POST) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            naver_id = str(post.naver_id) #사용자입력아이디
            naver_pw = str(post.naver_pw) #사용자입력비밀번호

            driver = webdriver.PhantomJS('/Users/HqPark/Desktop/naver_work/phantomjs-2.1.1-macosx 2/bin/phantomjs')
            driver.get('https://nid.naver.com/nidlogin.login')
            driver.find_element_by_name('id').send_keys(naver_id)
            driver.find_element_by_name('pw').send_keys(naver_pw)
            # 로그인버튼 클릭
            driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

            if driver.current_url == 'https://www.naver.com/':
                post.save()
                print('{} 네이버 아이디 유효'.format(naver_id))
                return redirect('idlist')

            else:
                print('{} 비밀번호가 맞지 않습니다.'.format(naver_id))
                form = NaverTaskForm(request.POST)

    else:
        form = NaverTaskForm() # An unbound form

    #todo:설정한 [naver_id,naver_pw],[cafe_address,cafe_board],[title,article,tags]를 받는다.
    #todo:얻은 값으로 로그인 > 카페접속 > 글쓰기 > 글작성완료 로직.

    context = {'idlists': idlists, 'cafelists': cafelists, 'postlists': postlists}


    return render(request, 'naver_work/task.html', context)

def idlist(request):
    idlist = NaverAccount.objects.all()
    query = request.GET.get('q')

    if query:
        idlist = idlist.filter(Q(naver_id__icontains=query))

    paginator = Paginator(idlist, 2)
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

            naver_id = str(post.naver_id) #사용자입력아이디
            naver_pw = str(post.naver_pw) #사용자입력비밀번호

            driver = webdriver.PhantomJS('/Users/HqPark/Desktop/naver_work/phantomjs-2.1.1-macosx 2/bin/phantomjs')
            driver.get('https://nid.naver.com/nidlogin.login')
            driver.find_element_by_name('id').send_keys(naver_id)
            driver.find_element_by_name('pw').send_keys(naver_pw)
            # 로그인버튼 클릭
            driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

            if driver.current_url == 'https://www.naver.com/':
                post.save()
                print('{} 네이버 아이디 유효'.format(naver_id))
                return redirect('idlist')

            else:
                print('{} 비밀번호가 맞지 않습니다.'.format(naver_id))
                form = NaverAccountForm(request.POST)

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
    paginator = Paginator(cafelist, 1)
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

def postlist(request, ):
    postlist = PostList.objects.all()
    query = request.GET.get('q')

    if query:
        postlist = postlist.filter(Q(title__icontains=query))

    paginator = Paginator(postlist, 100)
    page = request.GET.get('page')
    postlists = paginator.get_page(page)
    context = {'postlists': postlists, 'page': page}

    return render(request, 'naver_work/postlist.html', context)

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

    return render(request, 'naver_work/post_edit.html', context)

def post_detail(request, pk):
    post = get_object_or_404(PostList, pk=pk)
    context = {'post': post}

    return render(request, 'naver_work/post_detail.html', context)

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

    return render(request, 'naver_work/post_edit.html', context)
