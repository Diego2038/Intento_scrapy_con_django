from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from itemloaders.processors import TakeFirst, Identity
from scrapy.linkextractors import LinkExtractor
from scrapy_module.items import Computer
from itemadapter import ItemAdapter 

from asgiref.sync import sync_to_async #! OJO

import os
os.environ['DJANGO_SETTINGS_MODULE']='project_scrapy.settings'

from app_scrapy.models import Articulo
from app_scrapy.serializers import ArticuloSerializer

# class ArticuloLoader(ItemLoader):
#     default_item_class = Articulo
#     default_input_processor = TakeFirst()
    
#     titulo_in = Identity()
#     precio_in = Identity()
#     descripcion_in = Identity()
     

# class ArticuloAdapter(ItemAdapter):
#     def __init__(self, item):
#         super().__init__(item)
#         self.default_output_processor = TakeFirst()

class MercadolibrespiderSpider(CrawlSpider):
    name = "MercadoLibreSpider"
    allowed_domains = ['listado.mercadolibre.com.co', 'articulo.mercadolibre.com.co/', 'mercadolibre.com.co']
    start_urls = ["https://listado.mercadolibre.com.co/computadora-portatil#D[A:computadora%20portatil]"]
    
    
    # xd
    download_delay = 0.5 #!
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 3, #!
        'CLOSESPIDER_ITEMCOUNT': 3, #!
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
    def parser_computer(self, response):
        sel = Selector(response)
        item = ItemLoader(Computer(), sel)
        item.add_xpath('title','//h1[@class="ui-pdp-title"]//text()')
        item.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]//text()', MapCompose(self.clean_price))
        # item.add_xpath('description', '//p[@class="ui-pdp-description__content"]//text()')
        item.add_value('description','Descripción genérica')
        yield item.load_item()
        
        
    # def parser_computer(self, response):
    #     loader = ArticuloLoader(response=response) 
    #     loader.add_xpath('titulo','//h1[@class="ui-pdp-title"]//text()')
    #     loader.add_xpath('precio', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]//text()', MapCompose(self.clean_price))
    #     loader.add_xpath('descripcion', '//p[@class="ui-pdp-description__content"]//text()') 
    #     articulo = loader.load_item()
    #     print("AAAAAAAAAAAAAAAAAAAAHHHHHHHAAAAAAAAAAAA", articulo)
    #     articulo.save()
    
    
    # def parser_computer(self, response):
    #     loader = ArticuloLoader(response=response)
    #     articulo = loader.load_item()

    #     adapter = ItemAdapter(articulo)
    #     # articulo_django = Articulo()
        
    #     articulo_data = {}
        
    #     for field in Articulo._meta.fields:
    #         if field.name in adapter:
    #             # setattr(articulo_django, field.name, adapter.get(field.name))
    #             articulo_data[field.name] = adapter.get(field.name)
        
    #     serializer = ArticuloSerializer(data=articulo_data)
    #     if serializer.is_valid():
    #         serializer.save() 
    
    
    # def parser_computer(self, response):
        
    #     articulo = Articulo()
        
    #     adapter = adapter(articulo)
        
    #     adapter['titulo'] = response.xpath('//h1[@class="ui-pdp-title"]//text()').get()
    #     adapter['precio'] = '6667'
    #     adapter['descripcion'] = response.xpath('//p[@class="ui-pdp-description__content"]//text()').get()
    #     adapter.save()
    # xd

     
