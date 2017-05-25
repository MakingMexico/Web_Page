from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class Index2View(TemplateView):
    template_name = "index2.html"


class UsView(TemplateView):
    template_name = 'us.html'


class PythonView(TemplateView):
    template_name = 'python.html'


class RubyView(TemplateView):
    template_name = 'ruby.html'
