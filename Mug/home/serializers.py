from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Mug


class MugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mug
        fields = ['id', 'name', 'category',
                  'quantity', 'created_by', 'created_date', 'image', 'price']


class MugStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mug
        fields = ['id', 'name', 'created_by',
                  'created_date', 'category', 'quantity', 'image', 'price']
        extra_kwargs = {'name': {'read_only': True},
                        'created_by': {'read_only': True},
                        'created_date': {'read_only': True}}
        #read_only_fields = ['id', 'name', 'created_by', 'created_date']
