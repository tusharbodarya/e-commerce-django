from django.shortcuts import get_object_or_404, render
from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview
from taggit.models import Tag
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

def product_detail_view(request, pid):
    product = Products.objects.get(pid=pid)
    product_images = product.product_images.all()
    related_products = Products.objects.filter(category=product.category).exclude(pid=pid)
    context = {
        "product": product,
        "product_images": product_images,
        "related_products": related_products
    }
    return render(request,'core/product-detail.html',context)

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

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors":vendors
    }
    return render(request,'core/vendor-list.html',context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Products.objects.filter(product_status="published",vendor=vendor)
    context = {
        "vendor":vendor,
        "products":products
    }
    return render(request,'core/vendor-detail.html',context)

def tag_list_view(request, tag_slug=None):
    products = Products.objects.filter(product_status="published").order_by("-id")
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
        
    context = {
        "products":products,
        "tag":tag
    }
    
    return render(request,"core/tag-list.html",context)