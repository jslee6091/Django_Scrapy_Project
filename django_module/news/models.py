from django.db import models

class ItNews(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()

    class Meta:
        verbose_name = 'it_new'
        verbose_name_plural = 'it_news'
        db_table = 'news_itnews'

        ordering = ('-id',)
     
    def __str__(self):
        return self.title
