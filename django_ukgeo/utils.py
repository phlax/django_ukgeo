import logging

from geopy import geocoders
from geopy.geocoders.base import GeocoderResultError

from haystack.query import SearchQuerySet

log = logging.getLogger('django.request')


def save_place(name, lat, lng, label, model=None):
    if not model:
        from django_ukgeo.models import Place
        model = Place
    place = model.objects.create(name=name, label=label, lat=lat, lng=lng)
    place.save()


def geocode(keyword, cache=True, model=None, exactly_one=True):
    results = None

    if not model:
        from django_ukgeo.models import Place
        model = Place

    cached = SearchQuerySet().models(
        model).filter(name=keyword).order_by('-weight')

    if cached:
        if exactly_one:
            return cached[0].label, cached[0].location
        return ((c[0].label, c[0].location) for c in cached)

    g = geocoders.GoogleV3(domain='maps.google.co.uk')

    try:
        search_keyword = keyword
        if not keyword.endswith(' UK'):
            search_keyword = "%s UK" % keyword
        results = g.geocode(search_keyword, exactly_one=False)
    except GeocoderResultError:
        log.error('Geocoding failed (Geocoder result error): %s' % keyword)
    except ValueError:
        log.error('Geocoding failed (Value error): %s' % keyword)

    if not results:
        return None, (None, None)

    if cache:
        for place, (lat, lng) in reversed(results):
            save_place(keyword, lat, lng, place, model)

    if exactly_one:
        return results[0]
    return results

geocode_postcode = geocode
