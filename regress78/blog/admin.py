from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from blog.models import (
    TopMenu,
    Author,
    Tag,
    BlogItem,
    Adv,
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


class AdvAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'additional',
        'adv_position',
        'pic',
        'published',
        'date_published',
    )

admin.site.register(TopMenu, MenuItemAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BlogItem, BlogItemAdmin)
admin.site.register(Adv, AdvAdmin)
