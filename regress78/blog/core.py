from django.db import models
from django.db.models import F
from django.core.paginator import Paginator
from django.conf import settings


def paged(prepared_data, c_page):
    """
    :param prepared_data: data to paginate
    :param c_page: current page number
    :return: django.core.paginator.Paginator
    """
    p = Paginator(prepared_data, settings.BLOG_TOPICS_PER_PAGE)
    return p.page(c_page), p


class ListManager(models.Manager):

    def list_items(self, topic_type=0):
        return self.get_queryset().filter(published=True,
                                          topic_type=topic_type).order_by("-date_published")

    def by_id(self, topic_id):
        return self.get_queryset().filter(published=True, id=topic_id)

    @staticmethod
    def increment_view(blog_item):
        blog_item.update(hits=F('hits') + 1)
