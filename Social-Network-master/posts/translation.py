from modeltranslation.translator import TranslationOptions, register
from .models import Post, Like


@register(Post)
class PostsTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(Like)
class LikeTranslationOptions(TranslationOptions):
    fields = ('value',)