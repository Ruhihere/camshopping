from django.contrib import admin
from .models import Customer,Product,Order,Feedback
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','mobile','address','thumbnail_preview',)


    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description = 'Profile Pic'
    thumbnail_preview.allow_tags = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','thumbnail_preview',)
    list_editable=['price']

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description = 'Product Pic'
    thumbnail_preview.allow_tags = True
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','product','email','address','mobile','status','order_date',)
    list_editable=['status']
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','feedback',)
# Register your models here.
