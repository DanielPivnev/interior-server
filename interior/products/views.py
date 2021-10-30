from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from products.models import ProductsCategory, Product

# Create your views here.


def index(request):

    return render(request, 'products/index.html')


def products(request, c_id=0, page=1):
    filtered_products = Product.objects.filter(category_id=c_id) if c_id > 0 else Product.objects.all()
    paginator = Paginator(filtered_products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except EmptyPage:
        products_paginator = paginator.page(1)
    except PageNotAnInteger:
        products_paginator = paginator.page(paginator.num_pages)

    pages = [p for p in products_paginator.paginator.page_range][page - 3 if page > 3 else 0:page]
    last_page = [p for p in products_paginator.paginator.page_range][-1:]

    content = {
        'products': products_paginator,
        'categories': ProductsCategory.objects.all(),
        'pages': pages + last_page,
        'c_id': c_id
    }

    return render(request, 'products/products.html', content)
