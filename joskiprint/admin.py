from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, UserDetails, PrintOptions, Pricing
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=("file", "fileurl", "pages", "printOptions", "notes", "price", "userDetails", "status")
    fields=[("file", "fileurl"), ("pages", "printOptions", "notes"), "price", "userDetails", "status"]

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    pass

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(PrintOptions)
class PrintOptionsAdmin(admin.ModelAdmin):
    pass