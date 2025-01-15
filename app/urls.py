from django.urls import path
from .views import HomePageView, AboutPageView
from .views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from .views import BikeListView, BikeDetailView, BikeCreateView, BikeUpdateView, BikeDeleteView
from Corpuz import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    #Category
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),

    #Bike
    path('bike/', BikeListView.as_view(), name='bike_list'),
    path('bike/<int:pk>', BikeDetailView.as_view(), name='bike_detail'),
    path('bike/create', BikeCreateView.as_view(), name='bike_create'),
    path('bike/<int:pk>/edit', BikeUpdateView.as_view(), name='bike_update'),
    path('bike/<int:pk>/delete', BikeDeleteView.as_view(), name='bike_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)