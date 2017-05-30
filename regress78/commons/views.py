from django.views.generic import TemplateView
from blog.core import (
    fetch_menu,
    fetch_adv,
    fetch_stick_topics,
)
from django.conf import settings


class RegressView(TemplateView):

    def c_page(self, **kwargs):
        page = kwargs.get("page", None)
        if page is None:
            page = 1
        return page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "Regress78",
            'main_menu': fetch_menu(),
            'adv': fetch_adv(),
            'topic_stick_on_sidebar': fetch_stick_topics(),
            'media_path': settings.MEDIA_URL,
        })
        return context
