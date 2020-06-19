from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def landing(request):
    return render(request, 'shop/main_page.html')


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        p_list = Product.objects.filter(name__icontains=search_query)
    else:
        p_list = Product.objects.all()

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        p_list = products.filter(category=category)
    paginator = Paginator(p_list, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
    else:
            prev_url = ''

    if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
    else:
            next_url = ''


    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'page_object': page,
                                                      'is_paginated': is_paginated,
                                                      'next_url': next_url,
                                                      'prev_url': prev_url
                                                      })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})