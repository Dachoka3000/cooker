from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Recipe
from .serializers import RecipeSerializer



# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def recipe_list(request):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        # title = request.GET.get('title', None)
        #     if title is not None:
        #         recipes = recipes.filter(title__icontains=title)
            
        #     recipe_serializer = RecipeSerializer(recipes, many=True)
            # return JsonResponse(recipe_serializer.data, safe=False)
    elif request.method == 'POST':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse(recipe_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Recipe.objects.all().delete()
        return JsonResponse({'message': '{} Recipes were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'message': 'The recipe was not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        recipe_serializer = RecipeSerializer(recipe)
        return JsonResponse(recipe_serializer.data)
    elif request.method == 'PUT':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(recipe, data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse(recipe_serializer.data)
        return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

