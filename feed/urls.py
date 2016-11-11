from django.conf.urls import url
from . import views

app_name = 'feed'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^logout/$', views.logout_view, name='logout_view')
]