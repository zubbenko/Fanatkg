from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title