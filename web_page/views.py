from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class UsView(TemplateView):
    template_name = 'us.html'
