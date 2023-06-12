# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from itemadapter import adapter
from app_scrapy.models import Articulo #! TODO:


class ScrapyModuleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Articulo(Item): #! TODO:
    title = Field()
    price = Field()
    # description = Field()
