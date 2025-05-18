from django.db import models

# Create your models here.

class PostBlog(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='images/', blank=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
