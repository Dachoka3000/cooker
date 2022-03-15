from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions,filters,generics
from rest_framework.parsers import FileUploadParser
from django.http import Http404
from rest_framework import viewsets

from .models import Recipe
from .serializers import RecipeSerializer



# Create your views here.
#  @api_view(['GET', 'POST', 'DELETE'])
# def recipe_list(request):

#     if request.method == 'GET':
#         recipes = Recipe.objects.all()

#         # title = request.GET.get('title', None)
#         #     if title is not None:
#         #         recipes = recipes.filter(title__icontains=title)
            
#         #     recipe_serializer = RecipeSerializer(recipes, many=True)
#             # return JsonResponse(recipe_serializer.data, safe=False)
#     elif request.method == 'POST':
#         recipe_data = JSONParser().parse(request)
#         recipe_serializer = RecipeSerializer(data=recipe_data)
#         if recipe_serializer.is_valid():
#             recipe_serializer.save()
#             return JsonResponse(recipe_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         count = Recipe.objects.all().delete()
#         return JsonResponse({'message': '{} Recipes were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def recipe_detail(request, pk):
#     try:
    #    recipe = Recipe.objects.get(pk=pk)
    # except Recipe.DoesNotExist:
    #     return JsonResponse({'message': 'The recipe was not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == 'GET':
    #     recipe_serializer = RecipeSerializer(recipe)
    #     return JsonResponse(recipe_serializer.data)
    # elif request.method == 'PUT':
    #     recipe_data = JSONParser().parse(request)
    #     recipe_serializer = RecipeSerializer(recipe, data=recipe_data)
    #     if recipe_serializer.is_valid():
    #         recipe_serializer.save()
    #         return JsonResponse(recipe_serializer.data)
    #     return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     recipe.delete()
    #     return JsonResponse({'message': 'The recipe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



class RecipeList(APIView):

    parser_class = (FileUploadParser,)

    def get(self, request, format=None):
        all_recipes = Recipe.objects.all()
        serializers=RecipeSerializer(all_recipes, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = RecipeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(APIView):

    parser_class = (FileUploadParser,)

    def get_object(self,pk):
        '''
        retrieve recipe object from database
        '''

        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        get a single recipe object with its details
        '''

        recipe=self.get_object(pk)
        serializer=RecipeSerializer(recipe)
        return Response(serializer.data) 

    def put(self, request, pk, format=None):
        '''
        update details of a single recipe object
        '''

        recipe=self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()