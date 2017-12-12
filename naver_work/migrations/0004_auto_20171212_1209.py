# Generated by Django 2.0 on 2017-12-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naver_work', '0003_auto_20171211_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='naveraccount',
            name='naver_blog',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='naveraccount',
            name='naver_sex',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Men', max_length=10),
        ),
        migrations.AlterField(
            model_name='naveraccount',
            name='naver_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]