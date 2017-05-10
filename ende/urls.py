from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ende_page, name='ende_page')
]
