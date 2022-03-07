# 파서 함수 하나와 Rule, LinkExtractor 클래스를 사용하면 위키배과를 크롤링해서 문서 페이지를 모두 출력하고 나머지 페이지에는 표식만 남기는 스파이더를 만들 수 있음.

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AtricleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/',
                 'Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback = 'parse_items', follow = True, cb_kwargs = {'is_article': True}),
            Rule(LinkExtractor(allow = '.*'), callback = 'parse_items', cb_kwargs = {'is_article': False})]
    
    def parse_items(self, response):
        print(response.url)
        title = response.css('h1::text').extract_first()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ','')
            print(f'Title is: {title}')
            print(f'Last updated: {lastUpdated}')
            print(f'text is: {text}')
        else:
            print(f'This is not an article: {title}')
        
    def parse_items(self, response):
        print(response.url)
        title = response.css('h1::text').extract_first()
        if is_article:
            url = response.url
            
            text_rule = '//div[@id="mw-content-text"]//text()'
            text = response.xpath(text_rule).extract()

            updated_rule = 'li#footer-info-lastmod::text'
            update_delete = 'This page was last edited on'
            lastUpdated = response.css(update_relu).extract_first()
            lastUpdated = lastUpdated.replace(update_delete, '')

            print(f'Title is: {title}')
            print(f'Last updated: {lastUpdated}')
            print(f'text is: {text}')
        else:
            print(f'This is not an article: {title}')