from django.db import models

class Price(models.Model):
    hours = models.CharField(max_length=100)
    price = models.CharField(max_length=101)

    def __str__(self):
        return self.hours