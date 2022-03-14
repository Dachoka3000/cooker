from django.conf.urls import url 
from . import views

urlpatterns = [ 
    url(r'^api/recipes$', views.recipe_list),
    url(r'^api/recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
]
