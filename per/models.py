from django.db import models
from django.contrib.auth.models import User
from datetime import date



class post(models.Model):
    title = models.CharField('title', max_length=120)
    author = models.CharField('author', max_length=120)
    description = models.TextField('description')

    def __str__(self):
        return self.title

class about(models.Model):
    about_me = models.TextField('about')
    education = models.TextField('education')
    intrests = models.TextField('intrests')

