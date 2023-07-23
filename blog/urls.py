from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create_post/', views.create_post, name="create_post"),
    path('post_detail/<int:post_id>', views.post_detail, name="post_detail"),
]