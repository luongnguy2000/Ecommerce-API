import json
from django.http import JsonResponse
from rest_framework import views, viewsets, generics, mixins
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response


class ProductView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializers
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        query = Category.objects.get(id=pk)
        print(query)
        serializer = CategorySerializer(query)
        data_data = serializer.data
        all_data = []
        category_product = Product.objects.filter(category_id=data_data['id'])
        category_product_serializer = ProductSerializers(category_product, many=True)
        data_data['category_product'] = category_product_serializer.data
        all_data.append(data_data)
        return Response(all_data)