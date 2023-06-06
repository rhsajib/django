import json
# from django.shortcuts import render
from django.http import JsonResponse

from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    this is a django rest framework (DRF) api view
    """
    data = request.POST
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data =ProductSerializer(instance).data  # create dictionary data
    return Response(data)




@api_view(['GET'])
def api_home4(request, *args, **kwargs):
    """
    this is a django rest framework (DRF) api view
    """
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data =ProductSerializer(instance).data  # create dictionary data
    return Response(data)






@api_view(['GET'])
def api_home3(request, *args, **kwargs):
    """
    this is a django rest framework (DRF) api view
    """
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        # data = model_to_dict(model_data)
    return Response(data)



def api_home2(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        # data = model_to_dict(model_data)
    return JsonResponse(data)




def api_home1(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)

    body = request.body   # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)     # string of json data --> python dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)