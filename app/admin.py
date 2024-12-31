from django.contrib import admin
from .models import Category, Supplier, Bike, Customer, Order

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Bike)
admin.site.register(Customer)
admin.site.register(Order)
