from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)



class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request, item_id):
        cache_key = f'item_id_{item_id}'
        item = cache.get(cache_key)
        if not item:
            print(item)
            try:
                item = Item.objects.get(id=item_id)
                cache.set(cache_key, item, timeout=60 * 15)
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        print(item)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'item_id_{item_id}')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            cache.delete(f'item_id_{item_id}')
            return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

class ListItems(APIView):
    def get(self, request):
        cache_key="items"

        items=cache.get(cache_key)
        if not items:

            try:
                items=Item.objects.all()
                cache.set(cache_key,items,timeout=60*3)
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer=ItemSerializer(items,many=True)
        
        return Response(serializer.data)


# Below code is for testing redis whether it is working as expected.
import redis
redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
class TestRedisView(APIView):
    def get(self, request):
        # Set a value in Redis
        cache.set('test_key', 'Hello, Redis!', timeout=60)  # Key will expire after 60 seconds
        keys = redis_instance.keys('*')  # You can also use a specific pattern
        return Response({'cache_keys': [key.decode('utf-8') for key in keys]})
        
        