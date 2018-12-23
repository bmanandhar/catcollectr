from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('user/<username>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('<int:cat_id>/', views.show, name='show'),
    path('post_url/', views.post_cat, name='post_cat'),
    path('like_cat/', views.like_cat, name='like_cat'),
]
