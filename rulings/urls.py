from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<slug>[\w-]+)/$', 'rulings.views.show_ruling', name='show_ruling'),
)
