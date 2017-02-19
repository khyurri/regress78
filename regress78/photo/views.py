from django.shortcuts import render
from commons.views import RegressView
from photo.models import PhotoAlbumTree


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