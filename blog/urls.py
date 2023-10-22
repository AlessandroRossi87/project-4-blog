from . import views
from django.urls import path


urlpatterns = [
    path('new_post/', views.NewPost.as_view(), name='new_post'),
    path('', views.PostList.as_view(), name='home'),
    path('category/<str:category_name>/',
         views.category, name='category'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
