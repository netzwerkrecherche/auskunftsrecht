from django import forms

from haystack.forms import FacetedSearchForm


class RulingSearchForm(FacetedSearchForm):
    q = forms.CharField(
        required=False,
        label='Suche',
        widget=forms.TextInput(
            attrs={
                'type': 'search',
                'class': 'form-control',
                'placeholder': 'Ihre Sucheingabe'
            }))

    def search(self):
        return super(RulingSearchForm, self).search().highlight()
