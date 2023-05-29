from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Identity
from scrapy.linkextractors import LinkExtractor
from scrapy_module.items import Computer

import os
os.environ['DJANGO_SETTINGS_MODULE']='project_scrapy.settings'

from app_scrapy.models import Articulo

class ArticuloLoader(ItemLoader):
    default_item_class = Articulo
    default_input_processor = TakeFirst()
    
    titulo_in = Identity()
    precio_in = Identity()
    descripcion_in = Identity()
     


class MercadolibrespiderSpider(CrawlSpider):
    name = "MercadoLibreSpider"
    allowed_domains = ["listado.mercadolibre.com.co"]
    start_urls = ["https://listado.mercadolibre.com.co/computadora-portatil#D[A:computadora%20portatil]"]
    
    
    # xd
    download_delay = 1 #!
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20, #!
        #'CLOSESPIDER_ITEMCOUNT': 10 #!
    }
    
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/computacion/portatiles-accesorios/portatiles/'
            ), follow=True
        ),
        Rule(
            LinkExtractor( 
                allow=r'/laptop-'
            ), follow=True, callback='parser_computer' 
        ),
        Rule(
            LinkExtractor(
                allow=r'/MCO' 
            ), follow=True, callback='parser_computer'
        ), 
    )
    
    def clean_price(self, price:str):
       new_price = price.replace('$','').replace('.','')
       return float(new_price.strip())
    
    # Por si acaso
    # def parser_computer(self, response):
    #     sel = Selector(response)
    #     item = ItemLoader(Computer(), sel)
    #     item.add_xpath('title','//h1[@class="ui-pdp-title"]//text()')
    #     item.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]//text()', MapCompose(self.clean_price))
    #     item.add_xpath('description', '//p[@class="ui-pdp-description__content"]//text()')
    #     yield item.load_item()
        
    def parser_computer(self, response):
        loader = ArticuloLoader(response=response) 
        loader.add_xpath('title','//h1[@class="ui-pdp-title"]//text()')
        loader.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]//text()', MapCompose(self.clean_price))
        loader.add_xpath('description', '//p[@class="ui-pdp-description__content"]//text()')
        
        articulo = loader.load_item()
        articulo.save()
    # xd

     
