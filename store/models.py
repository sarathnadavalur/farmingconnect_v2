#from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    provider = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
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
    land_amount = models.IntegerField(default=2)
    soil_type = models.CharField(max_length=200, blank=True)
    coordinates =  models.CharField(max_length=200, blank=True)
    major_crop = models.CharField(max_length=200, blank=True)
    tenure_period = models.IntegerField(default=2)
    years_market = models.IntegerField(default=2)
    rating = models.IntegerField(default=2)
    deal_crops = models.CharField(max_length=200, blank=True)
    retail_type = models.CharField(max_length=200, blank=True)
    equipment_type = models.CharField(max_length=200, blank=True)
    equipment_name = models.CharField(max_length=500, blank=True)
    equipment_rent = models.IntegerField(default=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def grades(self):
        return super(VariationManager,self).filter(variation_category='grade',is_active=True)

    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_active=True)


variation_category_choice = {
    ('grade','grade'),
    ('size','size'),
}

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
