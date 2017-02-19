from django.views.generic import TemplateView
from blog.models import TopMenu


class RegressView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "Regress78",
            'main_menu': TopMenu.objects.filter(parent__isnull=True)
        })
        return context