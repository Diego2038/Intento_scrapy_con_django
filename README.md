# *Scrapy integration with Django Rest Framework*

This code is responsible for performing web scraping to the MercadoLibre page using the Scrapy library for data collection, and Django Restframework to store the data in a Postgres database.
<hr>

## Steps

To download the repository
```
git clone https://github.com/Diego2038/Attempt_scrapy_with_django
```

To create the virtual environment and download the libraries (if you don't have Windows, the process is different)
```
pip install venv
pip -m venv venv
/venv/Scripts/activate
pip install -r requirements.txt
```

To apply migrations to the Postgres database
```
python manage.py makemigrations
python manage.py migrate
```

To run the server

```
python manage.py runtime server
```

To run Scrapy, and have the information stored in the Django ORM DB:

```
python manage.py crawlxd
```

**Note**: The spiderejemplo.py file is kept for teaching purposes only, and has no relevance to code execution.