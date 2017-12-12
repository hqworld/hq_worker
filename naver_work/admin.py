from django.contrib import admin
from .models import NaverAccount, NaverCafeList, PostList
from django_summernote.admin import SummernoteModelAdmin



class PostListAdmin(SummernoteModelAdmin):
    pass

admin.site.register(NaverAccount)
admin.site.register(NaverCafeList)
admin.site.register(PostList, PostListAdmin)
