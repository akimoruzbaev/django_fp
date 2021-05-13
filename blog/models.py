from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
