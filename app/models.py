from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
