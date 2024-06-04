from django.shortcuts import render, redirect
from django.urls import reverse
from item.models import Items, Category
from .forms import CreateItemForm,EditItemForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    items = Items.objects.all()
    category = Category.objects.all()
    return render(request, 'item/index.html',{
        'items': items,
        'categories': category
    })

def detail(request, *args, **kwargs):
    id = kwargs.get('id')
    obj = Items.objects.get(id=id)
    return render(request, 'item/detail.html', {
        'item': obj
    })

@csrf_exempt
def create(request):
    if request.method == 'POST':
        form = CreateItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('item:detail', item.id)
    form = CreateItemForm()
    return render(request, "item/forms.html", {
        'form':form,
        "action":"create"
    })

def edit(request,**kwargs):
    print('INSIDE EDIT METHOD')
    print(kwargs)
    print(request.method)
    id = kwargs.get('id')
    instance = Items.objects.get(id=id)
    if request.method == 'POST':
        form = CreateItemForm(request.POST,instance=instance)
        if form.is_valid():
            item = form.save()
            return redirect("item:detail", item.id)
    form = CreateItemForm(instance=instance)
    print(form)
    return render(request, "item/forms.html", {
        "form": form,
        "action": "edit"
    })

def delete(request,**kwargs):
    id = kwargs.get('id')
    instance = Items.objects.get(id=id)
    instance.delete()
    return redirect(reverse('index'))
