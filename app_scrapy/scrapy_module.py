from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
# import scrapy
# from scrapy.contrib.djangoitem import DjangoItem
# from scra

# import views

class Computer(Item):
    title = Field()
    price = Field()
    description = Field()
    

class ComputerSpider( CrawlSpider ):
    name = "ComputerSpider"
    start_urls = ['https://listado.mercadolibre.com.co/computadora-portatil#D[A:computadora%20portatil]'] #!
    allowed_domains = ['listado.mercadolibre.com.co', 'articulo.mercadolibre.com.co/', 'mercadolibre.com.co'] #!
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
    
    def parser_computer(self, response):
        sel = Selector(response)
        item = ItemLoader(Computer(), sel)
        item.add_xpath('title','//h1[@class="ui-pdp-title"]//text()')
        item.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]//text()', MapCompose(self.clean_price))
        item.add_xpath('description', '//p[@class="ui-pdp-description__content"]//text()')
        
        
        yield item.load_item()
        
