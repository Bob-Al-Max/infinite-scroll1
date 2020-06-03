from django.urls import path, re_path

from . import views



urlpatterns = [
    
    path('posts/', views.post_list, name='post_list'),
    #re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),

    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:id>/', views.PostDetailView.as_view(), name='post-detail'),
    path('email/', views.ContactView.as_view(), name='email'),
    path('postadd/', views.PostCreate.as_view(), name='post-add'),
    re_path(r'^post-update/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='post-update'),
    re_path(r'^post-delete/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='post-delete'),
    path('sen/', views.sen, name='sen'),
    path('infinite/', views.PostsView.as_view(), name='posts'),
    
    
    
   
    
    
]



    


