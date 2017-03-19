from django.shortcuts import render, redirect
from commons.views import RegressView
from records.models import Records
from blog.core import paged


class RecordView(RegressView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "records/list.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.c_page(**kwargs)
        if page is "1":
            return redirect("/blog/")
        published = paged(Records.published_items.list_items(), page)
        context.update({
            "list": published,
        })
        return render(request, self.template_name, context)
