from django.db import models
from commons.core import UploadTo
from photo.core import ListManager
from mptt.models import (
    MPTTModel,
    TreeForeignKey
)


class PhotoAlbumTree(MPTTModel):

    published_items = ListManager()

    name = models.CharField('наименование (альбома или фото)', max_length=511)
    photo = models.ImageField(
        'фото',
        upload_to=UploadTo('photo'),
    )
    hits = models.PositiveIntegerField('просмотры', default=0)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='раздел'
    )
    published = models.BooleanField('опубликован', default=False)
    date_published = models.DateTimeField('дата публикации', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'
