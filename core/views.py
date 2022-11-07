from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


class BuildingsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Building.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("typeof", "city__slug", "category__slug")
    serializer_class = BulidingsSerializer
    lookup_field = "slug"


class CitiesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer


class HandPickViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = HandPick.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("building__category__slug",)
    serializer_class = HandPickSerializer


class ChatViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


@api_view()
def CategoriesView(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
