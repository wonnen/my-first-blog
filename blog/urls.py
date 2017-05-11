from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_page, name='blog_page'),
    url(r'new/$', views.post_new, name='post_new'),
]
