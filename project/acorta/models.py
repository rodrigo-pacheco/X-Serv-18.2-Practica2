from django.db import models

# Create your models here.

class URL(models.Model):
    url = models.URLField()
    def __str__(self):
        return self.url
