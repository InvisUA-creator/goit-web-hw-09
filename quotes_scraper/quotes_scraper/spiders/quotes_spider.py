import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page_url = response.css("li.next a::attr(href)").get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)
