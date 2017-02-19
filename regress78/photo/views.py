from django.shortcuts import render
from commons.views import RegressView
from photo.models import PhotoAlbumTree
from django.conf import settings


class PhotoList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "photo/list.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        galleries = PhotoAlbumTree.published_items.list_items()
        context.update({
            "galleries": galleries
        })
        return render(request, self.template_name, context)


class PhotoGallery(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "photo/gallery.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery_item = args[0]
        photos = PhotoAlbumTree.published_items.list_items(gallery_item)
        gallery = PhotoAlbumTree.published_items.by_id(gallery_item)
        context.update({
            "gallery": gallery.get(),
            "photos": photos,
            "media_path": settings.MEDIA_URL
        })
        return render(request, self.template_name, context)