from django.contrib import admin
from .models import NaverTask, NaverAccount, NaverCafeList, PostList


admin.site.register(NaverTask)
admin.site.register(NaverAccount)
admin.site.register(NaverCafeList)
admin.site.register(PostList)
