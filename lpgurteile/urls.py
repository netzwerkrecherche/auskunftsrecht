from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rulings.views import search

admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'lpgurteile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^$', search, name='haystack_search'),

    re_path(r'^urteil/', include('rulings.urls')),

    re_path(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def handler500(request):
    """
    500 error handler which includes ``request`` in the context.
    """

    from django.shortcuts import render
    return render(request, '500.html', {'request': request}, status=500)
