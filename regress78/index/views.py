from commons.views import RegressView
from blog.models import BlogItem
from django.shortcuts import render


class IndexView(RegressView):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "index/main.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        items_on_main = BlogItem.published_items.list_items(stick_on_main=True,
                                                            topic_type=0,)
        context.update({
            "list": items_on_main,
        })
        return render(request, self.template_name, context)
