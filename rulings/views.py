from urllib import urlencode
from urlparse import urlparse, parse_qsl

from django.shortcuts import render, get_object_or_404

from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

from .forms import RulingSearchForm
from .models import Ruling


default_sqs = (SearchQuerySet()
                .facet('court', order='term')
                .facet('jurisdiction', order='term')
                .facet('granted', order='term')
)


class RulingSearchView(FacetedSearchView):
    results_per_page = 15

    def extra_context(self):
        extra = super(RulingSearchView, self).extra_context()
        d = dict(parse_qsl(urlparse(self.request.get_full_path()).query))
        d.pop('page', None)
        extra['getvars'] = '&' + urlencode([
            (k.encode('utf-8'), v.encode('latin1')) for k, v in d.items()])
        return extra

search = RulingSearchView(form_class=RulingSearchForm,
                          searchqueryset=default_sqs)


def show_ruling(request, slug):
    obj = get_object_or_404(Ruling, slug=slug)
    return render(request, 'rulings/show.html', {'object': obj})
