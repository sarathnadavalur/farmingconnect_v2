from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    provider = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    mandal = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    pincode = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    available_brands = models.CharField(max_length=200, blank=True)
    price_per_kg = models.IntegerField()
    images = models.ImageField(upload_to='photos/products',blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name