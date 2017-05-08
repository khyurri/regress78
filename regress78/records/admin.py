from django.contrib import admin
from records.models import Records


class RecordsAdmin(admin.ModelAdmin):
    list_display = (
        "record_url",
        "pic",
        "title",
        "published",
        "date_published",
        "record_date",
        "stick_on_main",)
    filter_horizontal = ("dj", "tag",)

admin.site.register(Records, RecordsAdmin)
