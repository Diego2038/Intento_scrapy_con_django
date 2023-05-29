from django.contrib import admin
from django.urls import path, include
from app_scrapy import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api-auth/', include('rest_framework.urls')),
    path('articulo_post_post/', views.articulo_post, name='articulo_post_post')
  
]