from django.db import models
from django.db.models import F


class ListManager(models.Manager):

    def list_items(self, **kwargs):
        add_order = kwargs.get("add_order", None)
        order_by = ["-date_published"]
        if add_order is not None:
            order_by.append(add_order)

        return self.get_queryset().filter(published=True,
                                          **kwargs).order_by(*order_by)

    def by_id(self, topic_id, topic_type=0):
        return self.get_queryset().filter(published=True,
                                          id=topic_id,
                                          topic_type=topic_type)

    @staticmethod
    def increment_view(blog_item):
        blog_item.update(hits=F('hits') + 1)
