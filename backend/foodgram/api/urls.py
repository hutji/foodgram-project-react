from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, RecipeViewSet, TagViewSet, IngredientViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('recipes',RecipeViewSet, basename='recipes')
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
