from django.shortcuts import render


# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Articulo

# rest framework
from .serializers import ArticuloSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

# @csrf_exempt
# def articulo_post(request, articuloo=None):
#     try:
#         data = json.loads(request.body.decode('utf-8'))
         
#         articulo = Articulo()
#         articulo.titulo = data.get('titulo')
#         articulo.precio = data.get('precio')
#         articulo.descripcion = data.get('descripcion')
        
#         articulo.save() 
#         return JsonResponse({'status': "OK"}, status=200)
#     except Exception as e:
#         return JsonResponse({'status': "Error", 'reason': e}, status=400)  


@csrf_exempt
@api_view(['POST'])
def articulo_post(request):
    try: 
        serializer = ArticuloSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() 
        return Response(serializer.data, status= status.HTTP_201_CREATED )
    except BaseException as e:
        print(e)
        return Response(status= status.HTTP_400_BAD_REQUEST)


