from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import get_user_model
from .models import Category, Bike, Review, Supplier, Comment
from .forms import CommentForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_bikes = Bike.objects.filter(name__icontains=query)
        else:
            filtered_bikes = Bike.objects.all()
        context['bikes'] = filtered_bikes
        return context

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
        context['users'] = get_user_model().objects.all()
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

#Start of Comment CRUD
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    template_name = 'app/comments/comment_create.html'

    def form_valid(self, form):
        form.instance.bike_id = self.kwargs['pk']  # Assign the bike ID
        form.instance.username = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bike_detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'app/comments/comment_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the bike object to the context using the `bike_pk` from the URL
        context['bike'] = get_object_or_404(Bike, pk=self.kwargs['bike_pk'])
        return context

    def get_success_url(self):
        # Redirect to the `bike_detail` view after updating the comment
        return reverse_lazy('bike_detail', kwargs={'pk': self.kwargs['bike_pk']})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'app/comments/comment_delete.html'

    def get_object(self):
        # Find the comment based on `bike_pk` and `comment.pk`
        return get_object_or_404(Comment, pk=self.kwargs['pk'], bike__pk=self.kwargs['bike_pk'])

    def get_success_url(self):
        # Redirect to the bike's detail page after deleting the comment
        return reverse_lazy('bike_detail', kwargs={'pk': self.kwargs['bike_pk']})
#End of Comment CRUD

