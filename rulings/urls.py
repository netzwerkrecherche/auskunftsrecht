from django.conf.urls import re_path

from .views import show_ruling

urlpatterns = [
    re_path(r'^(?P<slug>[\w-]+)/$', show_ruling, name='show_ruling'),
]
