from django.shortcuts import render, redirect
from commons.views import RegressView
from video.models import Video
from blog.core import paged


class VideoItem(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "video/item.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.c_page(**kwargs)
        video = Video.published_items.by_id(page)
        context.update({
            "video": video.get(),
        })
        return render(request, self.template_name, context)


class VideoList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "video/list.html"

    def get(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        page = self.c_page(**kwargs)
        if page is "1":
            return redirect("/video/")
        data, pagination = paged(Video.published_items.list_items(), page)
        context.update({
            "list": data,
            "pagination": pagination,
        })
        return render(request, self.template_name, context)
