# Generated by Django 2.0 on 2017-12-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naver_work', '0008_auto_20171212_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naveraccount',
            name='naver_sex',
            field=models.CharField(choices=[('Men', '남자'), ('Men', '여자')], max_length=10),
        ),
    ]
