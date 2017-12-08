from django.shortcuts import render

# Create your views here.
def naver_work(request):
    return render(request, 'naver_work/naver_work.html', {})
