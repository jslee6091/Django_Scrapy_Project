from django.db import models

# Create your models here.
class WorldNews(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()

    class Meta:
        verbose_name = 'world_new'
        verbose_name_plural = 'world_news'
        db_table = 'world_news'

    def __str__(self):
        return self.title
