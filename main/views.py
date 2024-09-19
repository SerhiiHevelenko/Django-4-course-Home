from gettext import Catalog
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'ZamovHozky - Головна'
        context['content'] = 'Для замовлення перейдіть в "Каталог" та оберіть потрібні Вам товари'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'ZamovHozky - Про нас'
        context['content'] = 'Про нас'
        context['text_on_page'] = 'Текст про те, чому цей магазин такой класний.'
        return context
    





#def index(request):
#
#    context = {
#        'title': 'ZamovHozky - Головна',
#        'content': 'Для замовлення перейдіть в "Каталог" та оберіть потрібний Вам товар',
#    }
#    return render(request, 'main/index.html', context)



#def about(request):
#    context = {
#        'title': 'ZamovHozky - Про нас',
#        'content': "Про нас",
#        'text_on_page': "Текст про те, чому цей магазин такой класний."
#    }
#
#    return render(request, 'main/about.html', context)

