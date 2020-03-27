from django.contrib import admin
from product.models import Product
from apitest.models import Apitest, Apis

# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = ["apiname", "apiurl", "apiparamvalue", "apimethod", "aptresult", "apistatus", "create_time", "id", "product"]
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ["productname", "productdesc", "create_tiem", "id"]

admin.site.register(Product)

