from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess


class Command( BaseCommand ):
    def handle(self, *args, **kwargs):
        print('Oh hi mark')