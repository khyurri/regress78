from django.contrib import admin
from records.models import (
    Records,
    Track,
)


class RecordsAdmin(admin.ModelAdmin):
    list_display = (
        "record_url",
        "pic",
        "title",
        "published",
        "date_published",
        "record_date",
        "stick_on_main",)
    filter_horizontal = ("dj",
                         "tag",
                         "track",)


class TrackAdmin(admin.ModelAdmin):
    list_display = ("composer",
                    "song",)

admin.site.register(Records, RecordsAdmin)
admin.site.register(Track, TrackAdmin)
