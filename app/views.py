from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

#CategoryCRUD
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
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'app/category/category_update.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app/category/category_delete.html'
    success_url = reverse_lazy('category_list')