from django.conf.urls import url
from web_page.views import IndexView, ContactView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact_us/$', ContactView.as_view(), name='contact_us')
]
