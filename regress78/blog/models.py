from django.db import models
from commons.core import UploadTo
from tinymce_4.fields import TinyMCEModelField
from blog.managers import (
    ListManager
)

from mptt.models import (
    MPTTModel,
    TreeForeignKey
)


class MenuItem(MPTTModel):
    name = models.CharField("название", max_length=255)
    url = models.CharField("URL", max_length=255)
    order = models.IntegerField("сортировка", default=10)
    target = models.CharField(
        "аттрибут target",
        max_length=255,
        choices=(
            ("_self", "_self (default)"),
            ("_blank", "_blank"),
            ("_parent", "_parent"),
            ("_top", "_top"),
        ),
        default="",
    )
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        verbose_name="раздел"
    )

    def __str__(self):
        return "%s (%s)" % (self.name, self.url)

    class Meta:
        abstract = True


class TopMenu(MenuItem):
    class Meta:
        verbose_name = "пункт главного меню"
        verbose_name_plural = "пункты главного меню"


class Author(models.Model):
    name = models.CharField("имя", max_length=511)
    pic = models.ImageField(
        "аватар",
        upload_to=UploadTo("page"),
    )
    description = models.CharField("описание", max_length=2047)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"


class Tag(models.Model):
    name = models.CharField("Тег", max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class BlogItem(models.Model):

    published_items = ListManager()

    title = models.CharField("название", max_length=255)
    date_published = models.DateTimeField("дата публикации")
    published = models.BooleanField("опубликован", default=False)
    pic = models.ImageField(
        "изображение",
        upload_to=UploadTo("blog"),
        null=True,
        blank=True
    )
    preview = models.TextField("превью", default=None, null=True)
    content = TinyMCEModelField("текст поста", blank=True)
    position = models.IntegerField("позиция", default=500, db_index=True)
    hits = models.PositiveIntegerField("просмотры", default=0, db_index=True)
    creator = models.ForeignKey(Author,
                                verbose_name="автор",
                                related_name="%(app_label)s_creator",
                                default=None)

    topic_type = models.IntegerField(
        verbose_name="тип записи",
        choices=(
            (0, "Топик в блоге"),
            (1, "Событие")
        ),
        default=0
    )

    stick_on_main = models.BooleanField(verbose_name="закреплен на главной",
                                        default=False)

    stick_on_sidebar = models.BooleanField(verbose_name="закреплен в сайдбаре",
                                           default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "топик"
        verbose_name_plural = "топики"


class Adv(models.Model):

    list_manager = ListManager()

    pic = models.ImageField(
        "изображение",
        upload_to=UploadTo("adv"),
        null=True,
        blank=True
    )

    title = models.CharField("заголовок", max_length=128, default=None, null=True)
    description = models.CharField("описание", max_length=128, default=None, null=True)
    additional = models.CharField("дополнительно", max_length=128, default=None, null=True)

    adv_position = models.IntegerField(
        verbose_name="позиция баннера",
        choices=(
            (0, "в шапке"),
            (1, "слайдер на главной"),
            (2, "событие в сайдбаре"),
        ),
        default=0
    )

    date_published = models.DateTimeField("дата публикации", default=None, null=True)
    published = models.BooleanField(verbose_name="опубликован", default=False)
    adv_order = models.IntegerField(default=500, verbose_name="сортировка")
    link = models.CharField("ссылка", default=None, null=True, max_length=32)

    class Meta:
        verbose_name = "баннер"
        verbose_name_plural = "баннеры"
