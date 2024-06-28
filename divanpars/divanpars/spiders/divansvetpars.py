import scrapy


class DivansvetparsSpider(scrapy.Spider):
    name = "divansvetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        fixtures = response.css("div._Ud0k")
        for fixture in fixtures:
            yield {
                'name': fixture.css('div.wYUX2 span::text').get(),
                'price': fixture.css('div.pY3d2 span::text').get(),
                'url': "https://www.divan.ru" + fixture.css('a::attr(href)').get()
            }
