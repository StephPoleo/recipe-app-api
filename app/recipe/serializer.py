from django.forms import fields
from rest_framework import serializers
from core.models import Tag, Ingredients


class TagsSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id",)


class IngredientsSerializer(serializers.ModelSerializer):
    """Serializer for the ingredients"""

    class Meta:
        model = Ingredients
        fields = ("id", "name")
        read_only_fields = ("id",)
