# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# from app_scrapy.serializers import ArticuloSerializer
from asgiref.sync import sync_to_async
from scrapy.exceptions import DropItem

# import os
# os.environ['DJANGO_SETTINGS_MODULE']='project_scrapy.settings'

import logging

class ScrapyModulePipeline:
    
    
    
    async def process_item(self, item, spider):
        await self.save_item(item, spider)
        return item
    
    
    @sync_to_async
    def save_item(self, item, spider):
        
        try:
            articulo_data = {}
            articulo_data['price'] = item.get('price', [0])[0]
            articulo_data['title'] = item.get('title', ['Sin título'])[0]

            if articulo_data['title'] == 'Sin título':
                logging.warning("El elemento no contiene la clave 'title': %s", item)
                updated_item = {'title': 'Sin título', 'price': 0}
            else:
                updated_item = articulo_data

            item.update(updated_item) 

            print("MIRAAAAAAAAAA!!!!!!", articulo_data)

            
            # Realiza el proceso de guardado en la base de datos aquí
            print("SE GUARDÓ CORRECTAMENTE")
        except Exception as e: 
            print('Error:', e)
        
        return item

