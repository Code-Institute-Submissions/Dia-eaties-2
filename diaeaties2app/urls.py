from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('my_profile/', views.Profile.as_view(), name='profile'),
    path('create-recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/delete/', views.DeleteRecipe.as_view(), name='delete'),
    path('<slug:slug>/update/', views.UpdateRecipe.as_view(), name='update'),
    path('about', views.RecipeList.as_view(template_name="about.html"),
         name="about"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('love/<slug:slug>/', views.LovedRecipe.as_view(), name='loved_recipe'),
]
