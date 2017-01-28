from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from blog.models import (
    TopMenu,
    Author,
    Tag,
    BlogItem,
)


class MenuItemAdmin(DjangoMpttAdmin):
    list_display = ('name', 'url')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_published',
        'published',
        'position',
        'preview',
        'hits',
        'creator'
    )

admin.site.register(TopMenu, MenuItemAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BlogItem, BlogItemAdmin)