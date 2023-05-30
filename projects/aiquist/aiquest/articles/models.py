from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self) -> str:
        return self.title