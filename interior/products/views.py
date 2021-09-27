from django.shortcuts import render
from products.models import ProductsCategory, Product, ProductsSlidersImages, Contacts
from interior.settings import MEDIA_URL


# Create your views here.


def index(request):
    content = {
        'products': [
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=2).main_image)}',
                'title': Product.objects.get(id=2).title,
                'hover_icon_description': Product.objects.get(id=2).hover_icon_description
            },
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=3).main_image)}',
                'title': Product.objects.get(id=3).title,
                'hover_icon_description': Product.objects.get(id=3).hover_icon_description
            },
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=4).main_image)}',
                'title': Product.objects.get(id=4).title,
                'hover_icon_description': Product.objects.get(id=4).hover_icon_description
            }
        ]
    }

    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'categories': [category.name for category in ProductsCategory.objects.all()],
        'img': f'{MEDIA_URL}{str(Product.objects.get(id=1).main_image)}',
        'product_slider_imgs': [f'{MEDIA_URL}{str(slider.image)}' for slider in
                                ProductsSlidersImages.objects.filter(product_id=1)],
        'title': Product.objects.get(id=1).title,
        'action': Product.objects.get(id=1).action,
        'action_text': 'Горячие приджение',
        'price': Product.objects.get(id=1).price,
        'currency': 'руб',
        'description_texts': Product.objects.get(id=1).descriptions[2: -2].replace("','", "'").split("'"),
        'products': [
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=2).main_image)}',
                'title': Product.objects.get(id=2).title,
                'hover_icon_description': Product.objects.get(id=2).hover_icon_description
            },
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=3).main_image)}',
                'title': Product.objects.get(id=3).title,
                'hover_icon_description': Product.objects.get(id=3).hover_icon_description
            },
            {
                'img': f'{MEDIA_URL}{str(Product.objects.get(id=4).main_image)}',
                'title': Product.objects.get(id=4).title,
                'hover_icon_description': Product.objects.get(id=4).hover_icon_description
            }
        ]
    }

    return render(request, 'products/products.html', content)


def contact(request):
    content = {
        'locations': [
            {
                'city': Contacts.objects.get(id=1).city,
                'phone': Contacts.objects.get(id=1).phone,
                'email': Contacts.objects.get(id=1).email,
                'address': Contacts.objects.get(id=1).address
            },
            {
                'city': Contacts.objects.get(id=2).city,
                'phone': Contacts.objects.get(id=2).phone,
                'email': Contacts.objects.get(id=2).email,
                'address': Contacts.objects.get(id=2).address
            },
            {
                'city': Contacts.objects.get(id=3).city,
                'phone': Contacts.objects.get(id=3).phone,
                'email': Contacts.objects.get(id=3).email,
                'address': Contacts.objects.get(id=3).address
            }
        ]
    }

    return render(request, 'products/contact.html', content)
