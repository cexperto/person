from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, mixins
from .serializer import CustomUserSerializer
from .models import CustomUser
# Create your views here.


class CustomPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"


class CustomUserListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """
    view for creating and listing users
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomUserUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """
    view for get, update, and destroy a movie
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
