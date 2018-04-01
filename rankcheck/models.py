from django.db import models

class Text_input(models.Model):
    text = models.TextField('テキスト',max_length = 100)
    ownurl = models.URLField('URL',max_length = 200)
