from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from items.models import Inventory


def main(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'templates/index.html', context)


def items(request):
    title = 'Каталог оборудования'
    items_list = Inventory.objects.all()
    context = {
        'title': title,
        'items_list': items_list
    }
    return render(request, "invent/items.html", context)


def edit(request):
    title = 'Редактирование информации об абитуриенте'
    context = {
        'title': title,
        'links_menu': '',
        'category': '',
        'products': '',
    }
    return render(request, 'invent/edit.html', context)


def delete(request, pk):
    title = 'Удаление абитуриента'
    item_record = get_object_or_404(Inventory, pk=pk)
    item_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
