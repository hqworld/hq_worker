from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from taggit.managers import TaggableManager
from django_summernote import models as summer_model
from django_summernote import fields as summer_field

#네이버계정
class NaverAccount(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    naver_id = models.CharField(max_length=50, unique=True)
    naver_pw = models.CharField(max_length=200)
    sex = (('Men','남자'), ('Women','여자'))
    naver_sex = models.CharField(max_length=10, choices=sex)
    naver_nick = models.CharField(max_length=50, blank=True)
    naver_blog = models.URLField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.naver_id

    class Meta:
        ordering = ["-published_date"]


#네이버카페목록(todo: 아이디베이스로 가입카페목록 끌어오게할까? )
class NaverCafeList(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    cafe_name = models.CharField(max_length=50)
    cafe_address = models.URLField()
    cafe_board = models.CharField(max_length=50)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cafe_name

#3글 등록(텍스트에디터)
class PostList(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    title = models.CharField(max_length=50)
    article = summer_field.SummernoteTextField(default='내용을 입력해주세요.')
    published_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#실제 작업 로직(todo: 작업시간, 작업반복? 등 시간에 관련된것, 모듈화시키기)
class NaverTask(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    account = models.ManyToManyField(NaverAccount)
    cafe = models.ManyToManyField(NaverCafeList)
    post = models.ManyToManyField(PostList)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
