from django.shortcuts import render
from commons.views import RegressView
from video.models import Video


class VideoItem(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "video/item.html"


class VideoList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "video/list.html"
