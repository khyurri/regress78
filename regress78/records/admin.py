from django.contrib import admin
from records.models import Records


class RecordsAdmin(admin.ModelAdmin):
    list_display = ("record_url", "pic", "title", "published", "date_published")
    filter_horizontal = ("dj", "tag",)

admin.site.register(Records, RecordsAdmin)
