from django.db import models


class ListManager(models.Manager):

    def list_items(self, parent_id=None):
        kwargs = {
            "published": True,
        }
        if parent_id is None:
            kwargs["parent__isnull"] = True
        else:
            kwargs["parent"] = parent_id

        return self.get_queryset().filter(**kwargs).order_by("-date_published")

    def by_id(self, topic_id):
        return self.get_queryset().filter(published=True, id=topic_id)