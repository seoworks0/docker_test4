# Generated by Django 2.0.3 on 2018-05-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_auto_20180530_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='r_url',
            field=models.CharField(default='a', max_length=255, verbose_name='タイトル'),
        ),
        migrations.AddField(
            model_name='post',
            name='rank',
            field=models.CharField(default='b', max_length=255, verbose_name='タイトル'),
        ),
    ]