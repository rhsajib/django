from django.db import models
from django.utils import timezone

class Posts(models.Model):
    title = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    # creating new manager
    newmanager = models.Manager()

    def __str__(self):
        return self.title