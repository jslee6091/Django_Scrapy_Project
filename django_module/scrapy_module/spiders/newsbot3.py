import scrapy
from scrapy_module.items_world import ScrapyModuleItem
from scrapy.http import Request


# 세계 뉴스
URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=322&page=%s'
start_page = 1


def remove_space(descs:list) -> list:
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())

    return result


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot3'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]

    def start_requests(self):
        for i in range(5): # 0, 1 ~ 9 -> 1 ~ 10
            yield Request(url=URL % (i + start_page), callback=self.parse) # yield = 생성자 반환

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt/a/text()').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        titles_removed = remove_space(titles)

        items = []

        for idx in range(len(titles_removed)):
            item = ScrapyModuleItem()
            item['title'] = titles_removed[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)
        
        return items
