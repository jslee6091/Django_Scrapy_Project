from scrapy_djangoitem import DjangoItem
from world_news.models import WorldNews

class ScrapyModuleItem(DjangoItem):
    django_model = WorldNews
