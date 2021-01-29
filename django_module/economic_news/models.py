from django.db import models

# Create your models here.
class EconomicNews(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()

    class Meta:
        verbose_name = 'economic_new'
        verbose_name_plural = 'economic_news'
        db_table = 'economic_news'

    def __str__(self):
        return self.title
