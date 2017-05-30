from django.db import models
from commons.core import UploadTo
from blog.managers import ListManager


class Video(models.Model):

    published_items = ListManager()

    title = models.CharField("название", max_length=255)
    video_url_mp4 = models.CharField("ссылка на mp4 видео файл",
                                     max_length=10240, null=True)
    video_url_webm = models.CharField("ссылка на webm видео файл",
                                      max_length=10240, null=True)
    date_published = models.DateTimeField("дата публикации")
    published = models.BooleanField("опубликован", default=False)
    position = models.IntegerField("позиция", default=500, db_index=True)
    hits = models.PositiveIntegerField("просмотры", default=0, db_index=True)
    pic = models.ImageField(
        "превью видео",
        upload_to=UploadTo("blog"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "видео"
