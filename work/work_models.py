from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from taggit.managers import TaggableManager
from django_summernote import models as summer_model
from django_summernote import fields as summer_field

class Account(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    id = models.CharField(max_length=50, unique=True)
    pw = models.CharField(max_length=200)
    sexlist = (('Men','남자'), ('Women','여자'))
    sex = models.CharField(max_length=10, choices=sexlist)
    naver_nick = models.CharField(max_length=50, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.published_date = timezone.now()
        self.naver_pw = make_password(self.naver_pw)
        super(NaverAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["-published_date"]

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

class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    account = models.ManyToManyField(Account)
    post = models.ManyToManyField(PostList)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
