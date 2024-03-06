from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

SATUS_CHOICE = (
    ("proccess", "Proccessing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft","Draft"),
    ("disable","Disable"),
    ("rejected","Rejected"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATING = (
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
)

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Tags(models.Model):
    pass


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" heigth="50" />')

    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven")

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TimeField(null=True, blank=True)

    address = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    chat_res_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authantic_rating = models.CharField(max_length=100, default="100")
    day_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" heigth="50" />')

    def __str__(self):
        return self.title


class Products(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="prod")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TimeField(null=True, blank=True)

    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default="0.00")
    old_price = models.DecimalField(max_digits=9999999999, decimal_places=2, default="0.00")

    specifications = models.TimeField(null=True, blank=True)

    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")