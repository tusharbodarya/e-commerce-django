from django.shortcuts import render
from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview

# Create your views here.
def index(request):
    # products = Products.objects.all().order_by("-id")
    products = Products.objects.filter(product_status="published",featured=True).order_by("-id")
    context = {
        "products": products,
    }
    return render(request,'core/index.html',context)

def product_list_view(request):
    products = Products.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request,'core/product-list.html',context)

def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request,'core/category-list.html',context)

def category_products_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Products.objects.filter(product_status="published",category=category)
    
    context = {
        'products':products,
        'category':category
    }
    return render(request,'core/category-products-list.html',context)