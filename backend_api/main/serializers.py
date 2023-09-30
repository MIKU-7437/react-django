from rest_framework import serializers
from rest_framework.fields import empty
from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['user', 'address']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1
    

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class ProductListSeralizer(serializers.ModelSerializer):
    productrating_set = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields=['id', 'category', 'vendor', 'title', 'detail', 'price', 'productrating_set']
    
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['id','product','image']

class ProductDetailSerializer(serializers.ModelSerializer):
    product_rating = serializers.StringRelatedField(many=True, read_only=True)
    product_imgs = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields=['id', 'category', 'vendor', 'title', 'detail', 'price', 'tags', 'product_rating', 'product_imgs', 'demo_url']
    
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields=['id', 'user', 'mobile']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields=['id', 'user', 'mobile']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id', 'customer', 'address', 'default_address']
    
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields=['id', 'customer']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields=['id', 'order', 'product']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ['id', 'customer', 'product', 'rating', 'review', 'add_time']
    
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ['id', 'title', 'detail']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1
    

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ['id', 'title', 'detail']

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.Meta.depth = 1