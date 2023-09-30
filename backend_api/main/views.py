from typing import Any
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from . import serializers, models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSeralizer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            print(category)
            category = models.ProductCategory.objects.get(id=category)
            qs = qs.filter(category=category)
        return qs


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer

class RelatedProductSerilizer(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        product = models.Product.objects.get(id=product_id)
        queryset = models.Product.objects.filter(category=product.category).exclude(id=product_id)
        return queryset

class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer

@csrf_exempt
def customer_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    msg={}
    if user:
        msg={
            'bool':True,
            'user':user.username,
        }
        print(123123)
    else:
        msg={
            'bool':False,
            'msg':'Invalid User/Password',
        }
    return JsonResponse(msg)

@csrf_exempt
def customer_register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    mobile = request.POST['mobile']
    password = request.POST['password']
    try:
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password,
        )
        msg={}
        if user:
            try:
                customer = models.Customer.objects.create(
                    user=user,
                    mobile=mobile,
                )
                msg={
                    'bool':True,
                    'user':user.id,
                    'customer':customer.id,
                    'msg':'Thank you for registration. You can login'
                }
            except IntegrityError:
                msg={
                    'bool':False,
                    'msg':'Mobile already exists',
                }

        else:
            msg={
                'bool':False,
                'msg':'Opps',
            }
    except IntegrityError:
        msg={
                'bool':False,
                'msg':'Username is already exists',
            }
    return JsonResponse(msg)

class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerAddressSerializer
    queryset = models.CustomerAddress.objects.all()
    # def get_queryset(self):
    #     customer_id = self.kwargs['pk']
    #     customer = models.Customer.objects.get(id=customer_id)
    #     customer_address = models.CustomerAddress.objects.filter(customer=customer)
    #     return customer_address


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetail(generics.ListAPIView):
    # queryset = models.OrderProduct.objects.all()
    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        # return super().get_queryset()
        order_id = self.kwargs['pk']
        order = models.Order.objects.get(id=order_id)
        order_products = models.OrderProduct.objects.filter(order=order)
        return order_products
    

class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all()


class CategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategoryDetailSerializer