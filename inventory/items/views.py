from django.shortcuts import render

from django.http import HttpResponse

from items.models import Inventory


def index(request):
    title = 'Каталог оборудования'
    links_menu = Inventory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, "items/index.html", context)
