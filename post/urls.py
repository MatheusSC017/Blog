from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.Blog.as_view(), name='blog'),
    path('<int:pk>/', views.Post.as_view(), name='post'),
    path('meus_posts/', views.BlogUser.as_view(), name='user_blog'),
    path('cadastrar/', views.RegisterPost.as_view(), name='register_post'),
    path('atualizar/<int:pk>/', views.UpdatePost.as_view(), name='update_post'),
]
