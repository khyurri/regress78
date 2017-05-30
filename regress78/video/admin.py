from django.contrib import admin
from video.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'video_url_mp4',
        'video_url_webm',
        'pic',
        'published',
        'date_published',
        'position',
    )


admin.site.register(Video, VideoAdmin)
