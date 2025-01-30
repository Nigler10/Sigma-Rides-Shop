from django.urls import path
from .views import SignUp
from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),

    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
