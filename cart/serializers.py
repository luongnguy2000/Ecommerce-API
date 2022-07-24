from rest_framework import serializers
from .models import *

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1
        

class CartProductSerializer(serializers.Serializer):
    class Meta:
        model = CartProduct
        fields = '__all__'
        depth = 1
        