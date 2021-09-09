from django.shortcuts import render


# Create your views here.


def index(request):
    content = {
        'products': [
            {
                'img': 'img/product-1.jpg',
                'description_title': 'Отличный стул',
                'description': 'Расположитесь комфортно. '
            },
            {
                'img': '/img/product-2.jpg',
                'description_title': 'Отличный стул',
                'description': 'Расположитесь комфортно. '
            },
            {
                'img': 'img/product-1.jpg',
                'description_title': 'Отличный стул',
                'description': 'Расположитесь комфортно. '
            },
            {
                'img': '/img/product-2.jpg',
                'description_title': 'Отличный стул',
                'description': 'Расположитесь комфортно. '
            }
        ]
    }

    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'product_slider_imgs': ['img/controll.jpg', 'img/controll1.jpg', 'img/controll2.jpg'],
        'description_1': 'Отличный сту',
        'description_2': 'горячее предложение',
        'price': '2585.9',
        'currency': 'руб',
        'description_texts': ['Расположитесь комфортно.', 'Отличное качество материалов позволит вам это.',
                              'Различные цвета', 'высочайший уровеньэргономики и прочность.'],
        'products': [
            {
                'img': 'img/product-11.jpg',
                'description_title': 'Стул повышенного качества',
                'description': 'Не оторваться. '
            },
            {
                'img': 'img/product-21.jpg',
                'description_title': 'Стул повышенного качества',
                'description': 'Не оторваться. '
            },
            {
                'img': 'img/product-31.jpg',
                'description_title': 'Стул повышенного качества',
                'description': 'Не оторваться. '
            }
        ]
    }

    return render(request, 'products/products.html', content)


def contact(request):
    content = {
        'locations': [
            {
                'city': 'Москва',
                'phone_number': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            },
            {
                'city': 'Москва',
                'phone_number': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            },
            {
                'city': 'Москва',
                'phone_number': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            }
        ]
    }

    return render(request, 'products/contact.html', content)
