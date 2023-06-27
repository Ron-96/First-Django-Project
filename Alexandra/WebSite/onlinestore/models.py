from django.db import models


# Create your models here.

class AlbumTitleSuggestion(models.Model):
    title = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="RG Baby")
    date = models.DateTimeField()


def __str__(self):
    return self.title