from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import (
    Category,
    Product
)

def product_list(request, category_slug=None):
    """
    lista productos disponibles
    permite filtrar por una categoría
    """
    selected_category = None
    categories = Category.objects.all()
    products = Product.objects.available()

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
    return render(request, "shop/product/list.html", {
        "selected_category": selected_category,
        "categories": categories,
        "products": products
    })

def product_detail(request, id, slug):
    """
    muestra un unico producto
    """
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug
    )
    return render(request, "shop/product/detail.html", {
        "product":product
    })
