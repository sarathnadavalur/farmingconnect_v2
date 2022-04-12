from django.contrib import admin
from .models import Retailer
# Register your models here.
class RetailerAdmin(admin.ModelAdmin):
        list_display = ('retailer_name','license_number','years_in_market',)


admin.site.register(Retailer, RetailerAdmin)
