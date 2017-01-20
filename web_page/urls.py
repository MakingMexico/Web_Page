from django.conf.urls import url
from web_page.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^us/$', UsView.as_view(), name='us'),
    url(r'^python/$', PythonView.as_view(), name='python'),
    url(r'^ruby/$', RubyView.as_view(), name='ruby'),
]
