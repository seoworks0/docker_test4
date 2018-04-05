from django.db import models

class Suggest_input(models.Model):
    text = models.CharField('テキスト',max_length = 100)
