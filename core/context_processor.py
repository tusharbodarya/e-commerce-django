from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    try:
        address = Address.objects.get(user=request.user)
    except Exception:
        address = None
    return {
        "categories": categories,
        "address": address,
        "vendors": vendors
        }