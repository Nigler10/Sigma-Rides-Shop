from django.contrib import admin
from .models import Category, Supplier, Bike, Review, Customer, Order, Comment

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Bike)
admin.site.register(Review)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Comment)