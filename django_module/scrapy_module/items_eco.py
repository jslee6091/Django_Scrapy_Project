from scrapy_djangoitem import DjangoItem
from economic_news.models import EconomicNews

class ScrapyModuleItem(DjangoItem):
    django_model = EconomicNews
