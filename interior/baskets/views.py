from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from products.models import Product
from .models import Basket


# Create your views here.

@login_required
def basket_add(request, id):
    product = Product.objects.get(id=id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket.first().quantity += 1
        basket.first().save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        baskets = Basket.objects.get(id=id)

        if quantity > 0:
            baskets.quantity = quantity
            baskets.save()

        context = {
            'baskets': Basket.objects.filter(user=request.user)
        }

        result = render_to_string('baskets/basket.html' ,context)

        return JsonResponse({
            'result': result
        })

