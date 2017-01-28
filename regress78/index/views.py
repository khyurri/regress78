from commons.views import RegressView


class IndexView(RegressView):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "index/main.html"
        return super().dispatch(request, *args, **kwargs)
