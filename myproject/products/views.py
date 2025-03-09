from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .forms import ProductForm
from .pagination import StandardResultsSetPagination

# Create your views here.
def product_to_dict(product):
    return{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'price': str(product.price),
        'brand': product.brand,
        'quantity':str(product.quantity),
    }


class ProductViewSet(viewsets.ViewSet):
    pagination_class=StandardResultsSetPagination


    def list(self, request):
        products = Product.objects.all().order_by('name')
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request, view=self)
        product_list = [product_to_dict(product) for product in paginated_products]
        return paginator.get_paginated_response(product_list)
    

    def create(self, request):
        data = request.data.copy()
        form = ProductForm(data)
        if form.is_valid():
            product=form.save()
            return Response(product_to_dict(product), status=status.HTTP_200_OK)
        
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(product_to_dict(product))
    

    def update(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        form = ProductForm(request.data, instance=product)
        if form.is_valid():
            product=form.save()
            return Response(product_to_dict(product))
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


