from django.db import models
from django.utils import timezone
# Create your models here.
class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_Category = models.CharField(max_length=100)
    Product_Short_Description = models.TextField(max_length=100)
    Product_Full_Description = models.TextField(max_length=100)
    Product_Price = models.CharField(max_length=100)
    Product_Discount_price = models.CharField(max_length=100)
    Product_Tag = models.CharField(max_length=500)
    Product_Seo = models.CharField(max_length=500)
    Product_Unit = models.CharField(max_length=100, default='')
    Product_img = models.ImageField(upload_to='Products', max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Products.objects.get(id=self.id)
        except Products.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.Product_img and self.Product_img and obj.Product_img != self.Product_img:
            # delete the old image file from the storage in favor of the new file
            obj.Product_img.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.Product_img.delete()
        return super(Products, self).delete(*args, **kwargs)

class Addtocart(models.Model):
    user_id = models.CharField(max_length=100, default='')
    Product_id = models.CharField(max_length=100)
    Product_name = models.CharField(max_length=100)
    Product_Price = models.CharField(max_length=100)
    Product_Discount_price = models.CharField(max_length=100)
    Product_Unit = models.CharField(max_length=100, default='')
    Product_img = models.CharField(max_length=300, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Wishlist(models.Model):
    user_id = models.CharField(max_length=100, default='')
    Product_id = models.CharField(max_length=100)
    Product_name = models.CharField(max_length=100)
    Product_Price = models.CharField(max_length=100)
    Product_Discount_price = models.CharField(max_length=100)
    Product_Unit = models.CharField(max_length=100, default='')
    Product_img = models.CharField(max_length=300, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default='')
    qmessage = models.CharField(max_length=300, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    userid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=300, default='')
    payment = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default=timezone.now)

