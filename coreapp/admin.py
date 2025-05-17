from django.contrib import admin
from .models import Testimonial, Category, BlogPost, Project, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_at')
    search_fields = ('name', 'company', 'feedback')
    list_filter = ('created_at',)
    ordering = ('-created_at',)