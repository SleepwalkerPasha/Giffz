from django.contrib import admin
from .models import Post, Like
from modeltranslation.admin import TranslationAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(TranslationAdmin):
    pass


@admin.register(Like)
class LikeAdmin(TranslationAdmin):
    pass
