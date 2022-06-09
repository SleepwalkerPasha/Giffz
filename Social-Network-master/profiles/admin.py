from django.contrib import admin
from .models import Profile, Relationship
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(TranslationAdmin):
    pass


@admin.register(Relationship)
class RelationshipAdmin(TranslationAdmin):
    pass
