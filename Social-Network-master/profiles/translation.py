from modeltranslation.translator import TranslationOptions, register
from .models import Profile, Relationship


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'country', 'updated', 'created',)


@register(Relationship)
class RelationshipTranslationOptions(TranslationOptions):
    fields = ('status', 'updated', 'created',)
