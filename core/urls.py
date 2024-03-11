from django.urls import path
from core.views import index, category_list_view, product_list_view, product_detail_view, category_products_list_view, vendor_list_view, vendor_detail_view, tag_list_view, ajax_add_review, search_view, filter_products

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
]
