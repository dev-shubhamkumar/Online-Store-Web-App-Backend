from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')