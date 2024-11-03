from scrapy.crawler import CrawlerProcess
from quotes_scraper.quotes_scraper.spiders.quotes_spider import QuotesSpider
from quotes_scraper.quotes_scraper.spiders.authors_spider import AuthorSpider


process = CrawlerProcess()


process.crawl(QuotesSpider)
process.crawl(AuthorSpider)


process.start()
