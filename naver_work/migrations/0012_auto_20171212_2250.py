# Generated by Django 2.0 on 2017-12-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naver_work', '0011_postlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlist',
            name='article',
            field=models.TextField(max_length=50),
        ),
    ]
