from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new', views.recipe_new, name='recipe_new'),
    path('ingredient/new', views.IngredientNew.as_view(), name='ingredient_new'),
    path('recipe/edit/<int:pk>', views.RecipeUpdate.as_view(), name='recipe_edit'),
    path('recipe/delete/<int:pk>', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('registration/register/', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('registration/login', views.login_request, name='login'),
]

