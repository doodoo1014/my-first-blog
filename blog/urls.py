from django.urls import path 
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name="post_draft_list"),
    path('post/<pk>/puslish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('drafts/$', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/puslish/', views.post_publish, name='post_publish'),
]