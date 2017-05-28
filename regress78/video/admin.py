from django.contrib import admin
from video.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'video_url',
        'pic',
        'published',
        'date_published',
        'position',
    )

admin.site.register(Video, VideoAdmin)
