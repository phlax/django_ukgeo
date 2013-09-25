from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django_extensions.db.fields import AutoSlugField

from haystack.utils.geo import Point

from django_ukgeo.utils import geocode


class UKCity(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True)
    slug = AutoSlugField(populate_from='label')


class UKTown(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True)
    slug = AutoSlugField(populate_from='label')


class UKCounty(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True)
    slug = AutoSlugField(populate_from='label')


def save_postcode_location(postcode):
    try:
        location = postcode.location
    except ObjectDoesNotExist:
        print 'adding postcode!'
        location = PostcodeLocation(postcode=postcode)
    location.postcode = postcode
    location.save()


class Place(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    add_to_sitemaps = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_location(self):
        return Point(self.lat, self.lng)


class Postcode(models.Model):
    area = models.CharField(max_length=3)
    district = models.CharField(max_length=2)
    sector = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=2, blank=True, null=True)

    def __unicode__(self):
        return '%s%s %s%s' % (
            self.area.upper(),
            self.district.upper(),
            self.sector and self.sector or '',
            self.unit and self.unit.upper() or '')

    @property
    def placename(self):
        try:
            location = self.location
        except ObjectDoesNotExist:
            return ''
        if location:
            place = location.place
            if place.endswith(', UK'):
                return place[:-4]
            return place

    def get_location(self):
        try:
            location = self.location
        except ObjectDoesNotExist:
            return None
        return Point(location.lat, location.lng)

    @property
    def part1(self):
        return '%s%s' % (
            self.area.upper(),
            self.district.upper())

    def save(self, *la, **kwa):
        res = super(Postcode, self).save(*la, **kwa)
        save_postcode_location(self)
        return res

    # nasty hack!
    def get_absolute_url(self):
        return '/self-storage/%s' % self.__unicode__().replace(" ", "")


class PostcodeLocation(models.Model):
    postcode = models.OneToOneField(Postcode, related_name='location')
    place = models.CharField(max_length=255)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def save(self, *la, **kwa):
        place, (lat, lng) = geocode('%s UK' % str(self.postcode), cache=False)
        if place:
            self.place = place
            self.lat = lat
            self.lng = lng
            super(PostcodeLocation, self).save(*la, **kwa)

    def __unicode__(self):
        return self.place
