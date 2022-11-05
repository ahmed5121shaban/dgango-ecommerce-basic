
import datetime
from .models import Product, Brand, Category 
from rest_framework import serializers




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    #day = serializers.DateField(initial=datetime.date.today)
    #price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax_1')
    #def price_with_tax_1(self,product):
    #    return product.price*1.1

    class Meta:
        model = Product
        # many of field make mistake
        fields = '__all__'

