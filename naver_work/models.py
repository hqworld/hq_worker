from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

#네이버계정추가필드
class NaverAccount(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')
    naver_id = models.CharField(max_length=50, unique=True)
    naver_pw = models.CharField(max_length=200)
    sex = (('Men','남자'), ('Women','여자'))
    naver_sex = models.CharField(max_length=10, choices=sex)
    naver_nick = models.CharField(max_length=50, blank=True)
    naver_blog = models.URLField(null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)


    #naver_pw 비밀번호 형태로 저장
    def save(self, *args, **kwargs):
        self.published_date = timezone.now()
        self.naver_pw = make_password(self.naver_pw)
        super(NaverAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.naver_id

    class Meta:
        ordering = ["-published_date"]


#네이버카페목록추가필드
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
    article = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
