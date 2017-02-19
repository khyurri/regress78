from django.contrib import admin
from photo.models import (
    PhotoAlbumTree
)
from django_mptt_admin.admin import DjangoMpttAdmin


class PhotoAlbumAdmin(DjangoMpttAdmin):
    list_display = ('name', 'photo')


admin.site.register(PhotoAlbumTree, PhotoAlbumAdmin)