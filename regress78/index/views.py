from commons.views import RegressView
from blog.models import BlogItem
from records.models import Records
from django.shortcuts import render


class IndexView(RegressView):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "index/main.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_items = BlogItem.published_items.list_items(stick_on_main=True,
                                                         topic_type=0)
        records = Records.published_items.list_items(stick_on_main=True)
        context.update({
            "list": blog_items,
            "records": records,
        })
        return render(request, self.template_name, context)
