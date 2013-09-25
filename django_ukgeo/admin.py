from django.contrib import admin

from django_ukgeo.models import \
    UKCity, UKCounty, UKTown, Postcode, PostcodeLocation, Place


class PostcodeAdmin(admin.ModelAdmin):
    list_display = (
        "__unicode__", )


class PostcodeLocationAdmin(admin.ModelAdmin):
    list_display = (
        "__unicode__", )

    search_fields = (
        "place", )


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "name", "weight", "add_to_sitemaps", "label", "lat", "lng")

    list_editable = ("weight", "add_to_sitemaps", "label")

    search_fields = (
        "name", "label")


admin.site.register(UKCity)
admin.site.register(UKTown)
admin.site.register(UKCounty)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Postcode, PostcodeAdmin)
admin.site.register(PostcodeLocation, PostcodeLocationAdmin)
