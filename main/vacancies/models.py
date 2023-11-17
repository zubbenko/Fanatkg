from django.db import models

class Vacancies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    requirements = models.TextField(max_length=1000)
    contact = models.CharField(max_length=100)
    # link_google_form = models.URLField(blank=True)

    def __str__(self):
        return self.title

        