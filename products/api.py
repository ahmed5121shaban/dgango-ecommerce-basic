

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import ProductSerializer,BrandSerializer,CategorySerializer
from .models import Product,Brand,Category


@api_view(['GET'])
def product_list_api(request):
    list = Product.objects.all()
    json = ProductSerializer(list,many=True).data
    return Response({'status':200,'all product':json})

@api_view(['GET'])
def product_detail_api(request,id):
    list = Product.objects.get(id=id)
    json = ProductSerializer(list).data
    return Response({'status':200,'product':json})



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailApi(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer