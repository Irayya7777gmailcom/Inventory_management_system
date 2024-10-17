from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('items/', ItemCreateView.as_view(),name="items"),
    path('items/<int:item_id>/',ItemDetailView.as_view(),name="items"),
    path('ListItems/',ListItems.as_view(),name="ListItems"),
    path('test-redis/', TestRedisView.as_view(), name='test-redis'),
]
