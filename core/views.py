from django.shortcuts import get_object_or_404, render
from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview
from taggit.models import Tag
from django.db.models import Avg
from core.forms import ProductReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string
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
    reviews = ProductReview.objects.filter(product=product).order_by('-created_at')
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    review_form = ProductReviewForm()
    
    make_review = True
    
    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user,product=product).count()
        
        if user_review_count > 0:
            make_review = False
    
    context = {
        "product": product,
        "product_images": product_images,
        "related_products": related_products,
        "reviews": reviews,
        "average_rating": average_rating,
        "review_form": review_form,
        "make_review": make_review,
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

def ajax_add_review(request, pid):
    product = Products.objects.get(pk=pid)
    user = request.user
    
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST["review"],
        rating=request.POST["rating"]
    )
    
    
    context = {
        'user':user.username,
        'review':request.POST["review"],
        'rating':request.POST["rating"]
    }
    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    return JsonResponse({
        'status': True,
        'context': context,
        'average_reviews': average_reviews
    })
    
def search_view(request):
    query = request.GET.get('q')
    
    products = Products.objects.filter(title__icontains=query,description__icontains=query).order_by("-created_at")
    
    context = {
        'products':products,
        'query':query
    }
    
    return render(request, "core/search.html", context)


def filter_products(request):
    categories = request.GET.getlist('category[]')
    vendors = request.GET.getlist('vendors[]')
    
    products = Products.objects.filter(product_status="published").order_by('-id').distinct()
    
    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()
    
    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()
        
    context = {
        "products": products
    }
    data = render_to_string("core/async/product-list.html", context)
    
    return JsonResponse({'data':data})