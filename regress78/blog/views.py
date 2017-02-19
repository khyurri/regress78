from django.shortcuts import render
from commons.views import RegressView
from blog.models import BlogItem
from django.shortcuts import (
    render,
    redirect
)
from blog.core import paged
from django.conf import settings


class BlogList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "blog/list.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = kwargs.get("page", None)
        if page is "1":
            return redirect("/blog/")
        elif page is None:
            page = 1

        data, pagination = paged(BlogItem.published_items.list_items(), page)
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


class LightList(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "blog/light_list.html"

    def get(self, request, *args, **kwargs):
        topic_type = kwargs.get("topic_type", 0)
        context = super().get_context_data(**kwargs)
        data = BlogItem.published_items.list_items(topic_type)
        context.update({
            "detail_uri": kwargs.get("detail_item_uri"),
            "light_list": data,
        })
        return render(request, self.template_name, context)


class LightItem(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "blog/light_item.html"

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        topic_type = kwargs.get("topic_type", 0)
        blog_item = BlogItem.published_items.by_id(
            kwargs.get("id"), topic_type=topic_type)
        context.update({
            "light_topic": blog_item.get()
        })
        BlogItem.published_items.increment_view(blog_item)
        return render(request, self.template_name, context)