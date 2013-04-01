from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField('published on')
    body = models.TextField('Body', blank=True)

