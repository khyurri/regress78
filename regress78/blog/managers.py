from django.db import models
from django.db.models import F


class ListManager(models.Manager):

    def list_items(self, **kwargs):
        return self.get_queryset().filter(published=True,
                                          **kwargs).order_by("-date_published")

    def by_id(self, topic_id, topic_type=0):
        return self.get_queryset().filter(published=True,
                                          id=topic_id,
                                          topic_type=topic_type)

    @staticmethod
    def increment_view(blog_item):
        blog_item.update(hits=F('hits') + 1)
