from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('create-recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('<slug:slug>/delete/', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('<slug:slug>/update/', views.UpdateRecipe.as_view(), name='update_recipe'),
    path('love/<slug:slug>/', views.LovedRecipe.as_view(), name='loved_recipe'),
]
