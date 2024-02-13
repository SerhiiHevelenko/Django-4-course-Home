from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'ZamovHozky - Головна',
        'content': "ZamovHozky",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'ZamovHozky - Про нас',
        'content': "Про нас",
        'text_on_page': "Текст про те, чому цей магазин такой класний."
    }

    return render(request, 'main/about.html', context)