from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category


# def products_func(n):
#     products = [
#         {
#             'id': i,
#             'name': f'product {i}',
#             'price': i * 1000
#         } for i in range(n, n+5)
#     ]
#     return products
#
#
# categories = [
#     {
#         'id': i,
#         'name': f'category {i}',
#         'products': products_func(i)
#     } for i in range(1, 5)
# ]


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
# def product_list(request, n):
#     return JsonResponse(products_func(n), safe=False)


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        product_json = product.to_json()
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product does not exist'}, safe=False)
    return JsonResponse(product_json, safe=False)


def category_list(request):
    categories = Category.objects.all()
    cat_json = [category.to_json() for category in categories]
    return JsonResponse(cat_json, safe=False)


def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not exist'}, safe=False)
    return JsonResponse(category.to_json(), safe=False)


def cat_products(request, cat_id):
    try:
        products = Product.objects.filter(cat_id=cat_id)
        products_json = [product.to_json() for product in products]
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'products do not exist'}, safe=False)
    return JsonResponse(products_json, safe=False)
