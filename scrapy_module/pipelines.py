# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from app_scrapy.serializers import ArticuloSerializer
from asgiref.sync import sync_to_async
from scrapy.exceptions import DropItem

class ScrapyModulePipeline:
    
    @sync_to_async
    def save_item(self, item, spider):
        
        articulo_data = {}
        
        articulo_data['titulo'] = item['title'][0]
        articulo_data['precio'] = item['price'][0]
        articulo_data['descripcion'] = item['description'][0]
        # articulo_data['titulo'] = 'titulo'
        # articulo_data['precio'] = 1341
        # articulo_data['descripcion'] = 'Descripción genérica'
        
        print("MIRAAAAAAAAAA!!!!!!", articulo_data)
        try:
            
        
            serializer = ArticuloSerializer(data=articulo_data)
            if serializer.is_valid():
                instaciaxd = serializer.save()
                # await sync_to_async(serializer.save)()
                print("SE GUARDO CORRECTAMENTE YUPIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            else:
                raise DropItem(f"Item inválido: {serializer.errors}") 
        
        except Exception as e:
            print('Error pendejo:', e, '\n\n\n\n\n\n')
        
        finally:
            return item
    
    def process_item(self, item, spider):
        self.save_item(item)
        return item
