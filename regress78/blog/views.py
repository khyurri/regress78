from django.shortcuts import render
from commons.views import RegressView
from blog.models import BlogItem
from django.shortcuts import render
from blog.core import paged
from django.conf import settings


class BlogList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "blog/list.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data, pagination = paged(BlogItem.published_items.list_items(),
                                 kwargs.get("page", 1))
        context.update({
            "list": data,
            "pagination": pagination,
            "pagination_last":
                data.number + settings.BLOG_TOPICS_PAGE_SAMPLING_RANGE,
            "pagination_shown_last":
                pagination.num_pages - settings.BLOG_TOPICS_PAGE_SAMPLING_RANGE
        })
        return render(request, self.template_name, context)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BlogTopic(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "blog/topic.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        blog_item = BlogItem.published_items.by_id(args[0])
        context.update({
            "topic": blog_item.get()
        })
        BlogItem.published_items.increment_view(blog_item)
        return render(request, self.template_name, context)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)