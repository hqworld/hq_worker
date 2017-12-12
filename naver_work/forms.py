from django import forms
from .models import NaverAccount, NaverCafeList

class NaverAccountForm(forms.ModelForm):
    naver_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'아이디를 입력하세요.'}))
    naver_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'비밀번호를 입력하세요.'}))
    sex = (('Men','남자'), ('Women','여자'))
    naver_sex = forms.ChoiceField(choices=sex,widget=forms.Select(attrs={'class':'form-control'}))
    naver_nick = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'닉네임 결정하세요.'}))
    naver_blog = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'블로그 주소를 입력하세요.'}))
    
    class Meta:
        model = NaverAccount
        fields = ('naver_id', 'naver_pw', 'naver_sex', 'naver_nick','naver_blog',)

class NaverCafeListForm(forms.ModelForm):
    cafe_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'카페 이름'}))
    cafe_address = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'카페 주소'}))
    cafe_board = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'카페 글 남길 게시판'}))

    class Meta:
        model = NaverCafeList
        fields = ('cafe_name', 'cafe_address', 'cafe_board',)
