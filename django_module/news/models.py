from django.db import models

class ItNews(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()

    def __str__(self):
        return self.title
