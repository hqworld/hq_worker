# Generated by Django 2.0 on 2017-12-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naver_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naveraccount',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
