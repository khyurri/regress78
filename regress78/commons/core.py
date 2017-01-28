import os
import random
from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadTo(object):
    LENGTH = 11
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, directory):
        self.directory = directory

    def __call__(self, instance, filename):
        return self.generate_filename(filename)

    def generate_filename(self, filename):
        _, extension = os.path.splitext(filename)
        extension = extension.lower()
        while True:
            parts = [
                        random.choice(self.ALPHABET)
                        for _ in range(self.LENGTH)
                        ] + [extension]
            filename = ''.join(parts)
            upload_to = os.path.join(self.directory, filename)
            path = os.path.join(settings.MEDIA_ROOT, upload_to)
            if not os.path.exists(path):
                return upload_to