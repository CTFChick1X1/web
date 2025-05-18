from django.db import models

# Create your models here.

class PostBlog(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False, )
