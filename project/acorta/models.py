from django.db import models

# Create your models here.
# Superuser: rpacheco
# Password: 0000

class URL(models.Model):
    url = models.URLField()
    def __str__(self):
        return self.url
