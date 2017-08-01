from django.shortcuts import render

# Create your views here.


def index(request):
    context = dict()
    return render(request, 'menu/index.html', context)


def item(request, selected_item_id):
    context = dict(selected_item_id=selected_item_id)
    return render(request, 'menu/index.html', context)
