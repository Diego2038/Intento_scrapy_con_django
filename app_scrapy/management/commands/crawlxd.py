from django.core.management.base import BaseCommand
# from scrapy_module.spiders import MercadoLibreSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import scrapy

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        print('Inicializando scraping...')
        settings = get_project_settings()
        process = CrawlerProcess(settings)

        process.crawl('MercadoLibreSpider')
        process.start()
        # settings = get_project_settings()
        # settings.set('LOG_ENABLED', False ,priority='cmdline')
        
        # process = CrawlerProcess(settings)
        # process.crawl(MercadoLibreSpider)
        # process.start()