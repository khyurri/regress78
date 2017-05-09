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

    def by_id(self, item_id, **kwargs):
        return self.get_queryset().filter(published=True,
                                          id=item_id,
                                          **kwargs)

    @staticmethod
    def increment_view(blog_item):
        blog_item.update(hits=F('hits') + 1)
