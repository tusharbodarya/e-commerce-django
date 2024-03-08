from core.models import Products, Category, Vendor, CartOrder, CartOrderItems, Wishlist, Address, ProductImages, ProductReview

def default(request):
    categories = Category.objects.all()
    address = Address.objects.get(user=request.user)
    return {
        "categories": categories,
        "address": address
        }