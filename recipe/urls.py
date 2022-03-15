from django.urls import path
from . import views

urlpatterns = [
    # url(r'^api/recipes$', views.recipe_list),
    # url(r'^api/recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
    path('api/recipes/', views.RecipeList.as_view()),
    path('api/recipe/<int:pk>', views.RecipeDetail.as_view()),

]
