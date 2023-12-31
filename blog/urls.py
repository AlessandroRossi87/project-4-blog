from . import views
from django.urls import path
from django.conf.urls import handler404


urlpatterns = [
    path('new_post/', views.NewPost.as_view(), name='new_post'),
    path('edit/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path(
        'delete/<slug:slug>/', views.DeletePost.as_view(), name='post_delete'),
    path('', views.PostList.as_view(), name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

handler404 = 'blog.views.handler404'
