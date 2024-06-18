from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
]