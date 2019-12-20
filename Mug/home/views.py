from django.shortcuts import render
from .models import Mug
from .serializers import MugSerializer, MugStaffSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import ReadOnly
from rest_framework import filters

# Create your views here.


class MugList(generics.ListCreateAPIView):
    queryset = Mug.objects.all()
    serializer_class = MugSerializer
    permission_classes = [permissions.IsAdminUser | ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']
    ordering_fields = ['name']


# class MugSearch(generics.ListCreateAPIView):
#     #queryset = Mug.objects.all()
#     serializer_class = MugSerializer
#     permission_classes = [permissions.IsAdminUser | ReadOnly]

    # def get_queryset(self):
    #     category = self.kwargs['category']
    #     return Mug.objects.filter(category=category)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Mug.objects.filter(created_by=user)


class MugDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mug
    serializer_class = MugSerializer
    permission_classes = [permissions.IsAdminUser | ReadOnly]

    # def update(self, request, *args, **kwargs):
    #     user = request.user
    #     # if request.user.IsAdminUser:

    # if permissions.IsAdminUser:
    #     queryset = Mug
    #     serializer_class = MugSerializer
    #     permission_classes = [permissions.IsAdminUser | ReadOnly]

    # elif permissions.IsAuthenticatedOrReadOnly:
    #     queryset = Mug
    #     serializer_class = MugStaffSerializer
    #     permission_class = [permissions.IsAuthenticatedOrReadOnly]


class MugStaff(generics.RetrieveUpdateAPIView):
    queryset = Mug.objects.all()
    serializer_class = MugStaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
