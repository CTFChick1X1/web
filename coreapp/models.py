from django.db import models

# Create your models here.

class PostBlog(models.Model):
    name = CharField(max_length=50, blank=False)