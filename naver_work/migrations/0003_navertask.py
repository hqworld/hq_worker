# Generated by Django 2.0 on 2017-12-15 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('naver_work', '0002_auto_20171215_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naver_id', models.CharField(max_length=50, unique=True)),
                ('naver_pw', models.CharField(max_length=200)),
                ('cafe_name', models.CharField(max_length=50)),
                ('cafe_address', models.URLField()),
                ('cafe_board', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('article', django_summernote.fields.SummernoteTextField(default='내용을 입력해주세요.')),
                ('author', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
