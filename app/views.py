from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Category, Bike, Review, Supplier
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

#Start of Category CRUD
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categorys'
    template_name = 'app/category/category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'app/category/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'app/category/category_create.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'app/category/category_update.html'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app/category/category_delete.html'
    success_url = reverse_lazy('category_list')
#END of Category CRUD

#Start of Bike CRUD
class BikeListView(ListView):
    model = Bike
    context_object_name = 'bikes'
    template_name = 'app/bike/bike_list.html'

class BikeDetailView(DetailView):
    model = Bike
    context_object_name = 'bike'
    template_name = 'app/bike/bike_detail.html'

class BikeCreateView(CreateView):
    model = Bike
    fields = ['name', 'category', 'supplier', 'price', 'stock_quantity', 'image']
    template_name = 'app/bike/bike_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context

class BikeUpdateView(UpdateView):
    model = Bike
    fields = ['name', 'category', 'supplier', 'price', 'stock_quantity', 'image']
    template_name = 'app/bike/bike_update.html'

class BikeDeleteView(DeleteView):
    model = Bike
    template_name = 'app/bike/bike_delete.html'
    success_url = reverse_lazy('bike_list')
#End of Bike CRUD

#Start of Review CRUD
class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'app/reviews/review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'app/reviews/review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    fields = ['user', 'feedback']
    template_name = 'app/reviews/review_create.html'

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['user', 'feedback']
    template_name = 'app/reviews/review_update.html'

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'app/reviews/review_delete.html'
    success_url = reverse_lazy('review_list')
#End of Review CRUD

