from django.shortcuts import render
from item.models import Items, Category
# Create your views here.

def index(request):
    items = Items.objects.all()
    category = Category.objects.all()
    return render(request, 'item/items.html',{
        'items': items,
        'categories': category
    })