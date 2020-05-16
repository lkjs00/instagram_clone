from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'article', 'user']

admin.site.register(Article, ArticleAdmin)
admin.site.regitser(Comment)