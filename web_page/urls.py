from django.conf.urls import url
from web_page.views import IndexView, UsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^us/$', UsView.as_view(), name='us')
]
