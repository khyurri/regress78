from django.db import models


class ListManager(models.Manager):

    def list_items(self):
        return self.get_queryset().filter(published=True)

    def by_id(self, topic_id):
        return self.get_queryset().filter(published=True, id=topic_id)
