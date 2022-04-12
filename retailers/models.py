from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Retailer(models.Model):
    retailer_name = models.CharField(max_length=200)
    retailer_id = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
    address = models.TextField(max_length=500, blank=True)
    years_in_market = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    crops = models.CharField(max_length=200, blank=True)
    min_quality_grade = models.CharField(max_length=10, blank=True)
    payment_modes = models.CharField(max_length=200, blank=True)
    images = models.ImageField(upload_to='photos/products',blank=True)
    max_loan_sanction = models.CharField(max_length=10, blank=True)
    mortgage_required = models.BooleanField(blank=True)
    loan_approval_successrate = models.CharField(max_length=10, blank=True)
    rate_of_interest = models.CharField(max_length=10, blank=True)
    sanction_period = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.retailer_name

