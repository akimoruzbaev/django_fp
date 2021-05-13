from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    clipped_text = models.TextField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.title}'
