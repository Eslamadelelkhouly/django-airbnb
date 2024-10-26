from django.urls import path
from . import views
from .api_view import post_list_api


app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>',views.PostDetail.as_view(), name='post_detail'),
    path('category/<str:slug>',views.PostByCategory.as_view(), name='post_by_category'),
    path('tags/<slug:slug>',views.PostByTags.as_view(), name='post_by_tags'),

    ## API

    path('api/list', post_list_api, name='post_list_api'),
]
