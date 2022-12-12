from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Product
from cart.forms import CartAddProductForm
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ImageForm
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request,
                  'products.html',
                  {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product': product, 'cart_product_form': cart_product_form})

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_new.html'
    login_url = 'login'
    fields = ['name', 'price', 'image', 'description']

def ProductDelete(request, pk):
    product = models.Product.objects.get(id=pk)
    product.delete()
    return HttpResponse(reverse_lazy ('product_list'))

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    fields = ['name', 'price', 'image', 'description']
    template_name = 'product_edit.html'
    login_url = 'login'

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'product_new.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'product_new.html', {'form': form})


