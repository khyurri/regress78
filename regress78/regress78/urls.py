from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from filebrowser.sites import site as filebrowser_site
from index.views import IndexView
from django.conf import settings
from blog.views import (
    BlogList,
    BlogTopic,
    LightList,
    LightItem
)
from photo.views import (
    PhotoList,
    PhotoGallery,
)
from records.views import (
    RecordList,
    RecordItem,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^blog/$', BlogList.as_view(), name='blog_list'),
    url(r'^blog/(?P<page>[0-9]+)/$', BlogList.as_view(), name='blog_list'),
    url(r'^blog/topic/([0-9]+)/$', BlogTopic.as_view(), name='blog_topic'),
    url(r'^photo/$', PhotoList.as_view(), name='photo_list'),
    url(r'^photo/gallery/([0-9]+)/$', PhotoGallery.as_view(), name='photo_gallery'),
    url(r'^events/$', LightList.as_view(), {"name": 'event_list',
                                            "topic_type": 1,
                                            "detail_item_uri": "/event/date/"}),
    url(r'^event/date/(?P<id>[0-9]+)/', LightItem.as_view(), {"name": 'event_item',
                                                              "topic_type": 1}),
    url(r'^records/$', RecordList.as_view()),
    url(r'^records/(?P<page>[0-9]+)/$', RecordList.as_view()),
    url(r'^record/([0-9]+)/$', RecordItem.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
