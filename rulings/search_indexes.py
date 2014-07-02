from haystack import indexes

from .models import Ruling


class RulingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    file_reference = indexes.CharField(model_attr='file_reference')
    date = indexes.DateTimeField(model_attr='date', null=True)
    court = indexes.CharField(model_attr='court', faceted=True)
    jurisdiction = indexes.CharField(model_attr='jurisdiction', faceted=True)
    granted = indexes.CharField(model_attr='granted', faceted=True)
    subject = indexes.CharField(model_attr='subject')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Ruling

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
