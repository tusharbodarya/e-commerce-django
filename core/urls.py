from django.urls import include, path
from core.views import index, category_list_view, product_list_view, product_detail_view, category_products_list_view, vendor_list_view, vendor_detail_view, tag_list_view, ajax_add_review, search_view, filter_products, add_to_cart, cart_view, delete_item_from_cart, update_item_from_cart, checkout_view, payment_completed_view, payment_failed_view, customer_dashboard

app_name = "core"
urlpatterns = [
    # Dashboard
    path("",index,name="index"),
    
    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_products_list_view, name="category-products-list"),
    
    # Products
    path("products/", product_list_view, name="product-list"),
    path("products/<pid>/", product_detail_view, name="product-detail"),
    
    # Tags
    path("products/tag/<tag_slug>/", tag_list_view, name="tag-list"),
    
    # Vendors
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),
    
    # add review
    path("ajax-add-review/<pid>/", ajax_add_review, name="ajax-add-review"),
    
    # search view
    path("search/",search_view,name="search"),
    
    # filter products
    path("filter-product/",filter_products,name="filter-product"),
    
    # add-to-cart
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    
    # cart-view
    path("cart/", cart_view, name="cart"),
    
    # delete cart items
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),

    # update cart items
    path("update-from-cart/", update_item_from_cart, name="update-from-cart"),
    
    # checkout page
    path("checkout/", checkout_view, name="checkout"),
    
    # paypal payment
    path("paypal/",include('paypal.standard.ipn.urls')),
    
    # payment successfull
    path("payment-completed/", payment_completed_view, name="payment-completed"),
    
    # payment failed
    path("payment-failed/", payment_failed_view, name="payment-failed"),
    
    # user dashboard
    path("dashboard/", customer_dashboard, name="dashboard"),
]
