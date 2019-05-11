from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new', views.recipe_new, name='recipe_new'),
   # path('register', views.UserFormView.as_view(), name='register')
]

