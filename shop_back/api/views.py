from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from api.models import Product, Category


def product_list(request):
    ps = Product.objects.all()
    ps_json = [product.to_json() for product in ps]
    return JsonResponse(ps_json, safe=False)


def product_detail(request, product_id):
    try:
        ps = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(ps.to_json())


def category_list(request):
    cs = Category.objects.all()
    cs_json = [c.to_json() for c in cs]
    return JsonResponse(cs_json, safe=False)


def category_detail(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(c.to_json())


def category_products(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    products = c.product_set.all()
    ps_json = [p.to_json() for p in products]
    return JsonResponse(ps_json, safe=False)
