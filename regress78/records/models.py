from django.db import models
from commons.core import UploadTo
from blog.managers import ListManager
from blog.models import (
    Author,
    Tag,
)


class Track(models.Model):

    composer = models.CharField(max_length=1024,
                                verbose_name="исполнитель")
    song = models.CharField(max_length=1024,
                            verbose_name="песня")

    def __str__(self):
        return self.composer + " — " + self.song

    class Meta:
        verbose_name = "композиция"
        verbose_name_plural = "композиции"


class Records(models.Model):

    published_items = ListManager()

    record_url = models.CharField(max_length=1024,
                                  null=False,
                                  verbose_name="ссылка на запись")
    title = models.CharField(max_length=1024,
                             verbose_name="название")

    published = models.BooleanField(default=False,
                                    verbose_name="активен")
    date_published = models.DateTimeField(auto_now=True)

    record_date = models.DateTimeField(default="2017-01-01", verbose_name="дата эфира")

    pic = models.ImageField(
        'обложка',
        upload_to=UploadTo('records'),
        null=True,
        blank=True
    )
    dj = models.ManyToManyField(Author,
                                verbose_name="DJ",
                                default=None)

    tag = models.ManyToManyField(Tag,
                                 verbose_name="теги")

    track = models.ManyToManyField(Track,
                                   verbose_name="треки")

    stick_on_main = models.BooleanField(verbose_name="закреплен на главной",
                                        default=False)

    class Meta:
        verbose_name = "запись эфира"
        verbose_name_plural = "записи эфиров"

