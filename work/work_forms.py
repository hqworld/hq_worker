from django import forms
from .models import Task, Account, PostList
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from taggit.forms import *

class AccountForm(forms.ModelForm):
    id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'아이디를 입력하세요.'}))
    pw = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'비밀번호를 입력하세요.'}))
    sex = (('Men','남자'), ('Women','여자'))
    sex = forms.ChoiceField(choices=sex,widget=forms.Select(attrs={'class':'form-control'}))
    nick = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'닉네임 결정하세요.'}))

    class Meta:
        model = Account
        fields = ('id', 'pw', 'sex', 'nick',)


class PostListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'제목'}))
    article = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '400px'}))
    class Meta:
        model = PostList
        fields = ('title', 'article','tags',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('account','post',)
