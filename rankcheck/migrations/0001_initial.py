# Generated by Django 2.0.3 on 2018-03-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, verbose_name='テキスト')),
                ('ownurl', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
