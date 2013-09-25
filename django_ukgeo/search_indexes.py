from haystack import indexes
from haystack.indexes import \
    CharField, LocationField, IntegerField, BooleanField

from django_ukgeo.models import Postcode, Place


class PostcodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = CharField(document=True)

    area = CharField(model_attr="area")
    district = CharField(model_attr="district")
    part1 = CharField(model_attr="part1")
    placename = CharField(model_attr="placename")
    location = LocationField(model_attr="get_location")

    def get_model(self):
        return Postcode


class PlaceIndex(indexes.SearchIndex, indexes.Indexable):
    text = CharField(document=True)
    name = CharField(model_attr="name")
    label = CharField(model_attr="label")
    location = LocationField(model_attr="get_location")
    weight = IntegerField(model_attr="weight")
    add_to_sitemaps = BooleanField(model_attr="add_to_sitemaps")

    def get_model(self):
        return Place
