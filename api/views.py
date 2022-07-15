from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serlializers import ItemSerializer
from .models import Item

# Create your views here.
class ListapiAPIView(ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView):
    """This endpoint list all of the available apis from the database"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# class CreateapiAPIView(CreateAPIView):
#     """This endpoint allows for creation of a api"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class UpdateapiAPIView(UpdateAPIView):
#     """This endpoint allows for updating a specific api by passing in the id of the api to update"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class DeleteapiAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific api from the database"""
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer