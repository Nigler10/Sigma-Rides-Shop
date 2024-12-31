from django.urls import path
from .views import HomePageView, AboutPageView
from .views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
]