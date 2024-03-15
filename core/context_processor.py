from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview
from django.db.models import Min, Max

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    
    min_max_price = Products.objects.aggregate(Min("price"),Max("price"))
    try:
        wishlist = Wishlist.objects.filter(user=request.user)
    except Exception:
        wishlist = 0
    try:
        address = Address.objects.get(user=request.user)
    except Exception:
        address = None
    return {
        "categories": categories,
        "address": address,
        "vendors": vendors,
        "min_max_price": min_max_price,
        "wishlist": wishlist,
        }