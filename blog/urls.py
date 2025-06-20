from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Post URLs
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Comment URLs
    path('posts/<int:pk>/comment/', views.add_comment, name='add_comment'),
] 