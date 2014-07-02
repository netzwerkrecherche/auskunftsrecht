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
    pass

search = RulingSearchView(form_class=RulingSearchForm,
                          searchqueryset=default_sqs)


def show_ruling(request, slug):
    obj = get_object_or_404(Ruling, slug=slug)
    return render(request, 'rulings/show.html', {'object': obj})
