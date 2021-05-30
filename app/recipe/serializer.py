from core.models import Recipe
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


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredients.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = ("id", "title", "ingredients", "tags", "time_minutes", "price", "link")
        read_only_fields = ("id",)


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""

    ingredients = IngredientsSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
