from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display=['id','title','category','image','description','selling_price','artist_name']
admin.site.register(Comment)
admin.site.register(profile)
admin.site.register(urequesr)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(artistname)

# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','product','quantity']
