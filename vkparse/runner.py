from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from vkparse import settings
from vkparse.spiders.vk import VkSpider


if __name__ == '__main__':
    scr_settings = Settings()
    scr_settings.setmodule(settings)
    scr_settings.setmodule(settings)
    process = CrawlerProcess(settings=scr_settings)
    process.crawl(VkSpider)
    process.start()