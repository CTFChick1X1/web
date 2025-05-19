from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This classifies blogs ang different categorie .i.e Tech, Security, Network, Fasion
class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

# Hold data for different Blog
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    #Generate link url from the models title and save to slug before saving to database
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-').lower()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title

# Portfolio Models and Pojects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    project_image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # Generate link url from the models title and save to slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-').lower()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    
# saves user comments 
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.name}"

# what user says about us and their experience
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.company or 'No Company'}"