```
pip install venv
pip -m venv venv
pip install -r requirements.txt
```


Si se quiere comprobar que el scrapy por sí solo funciona:
```
cd scrapy_module/spiders
```

```
scrapy runspider MercadoLibreSpider.py -o prueba123.json
```
*Ahí debería de mosrtarte algunos datos guardados en el json* 

Si se quiere probar Scrapy con Django, vuelva a la carpeta raíz y aplique este comando:
```
python manage.py runserver
```

```
scrapy crawler MercadoLibreSpider
```

