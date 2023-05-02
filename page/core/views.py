from itertools import product
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewProductForm, EditProductForm
from .models import Category, Product

from django.shortcuts import render, redirect

from .forms import SignupForm

def index(request):
    product = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'products' : product,
        'categories': categories,
    }) 

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter().exclude(pk=pk)[0:3]

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            return redirect('product_detail', pk=product.id)
    else:
        form = NewProductForm()

    return render(request, 'newProduct.html', {
        'form': form,
        'title': 'New item',
    })

def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('product_detail', pk=product.id)
    else:
        form = NewProductForm(instance=product)

    return render(request, 'newProduct.html', {
        'form': form,
        'title': 'Edit item',
    })

def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            return redirect('product_detail', pk=product.id)

    else:
        form = NewProductForm()

    return render(request, 'newProduct.html', {
        'form': form,
        'title': 'New item',
    })

def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')