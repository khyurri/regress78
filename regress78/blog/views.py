from django.shortcuts import render
from commons.views import RegressView
from blog.models import BlogItem
from django.shortcuts import render


class BlogList(RegressView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "list": BlogItem.published_items.list_items()
        })
        return context

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog/list.html"
        return super().dispatch(request, *args, **kwargs)


class BlogTopic(RegressView):

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "topic": BlogItem.published_items.by_id(args[0]).get()
        })

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog/topic.html"
        return super().dispatch(request, *args, **kwargs)