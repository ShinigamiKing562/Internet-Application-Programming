from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_recipes, name='search_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]