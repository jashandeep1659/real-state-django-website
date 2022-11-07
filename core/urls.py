from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("projects", BuildingsViewSet, basename="buildings")
router.register("cities", CitiesViewSet, basename="cities")
router.register("handpicks", HandPickViewSet, basename="handpicked")
router.register("chat", ChatViewSet, basename="chat")
urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoriesView, name="categories"),
]
