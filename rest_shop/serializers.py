from django.contrib.auth.models import User, Group
from rest_framework import serializers
from shop.models import Dish, Cart, Company, Category, CartContent, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('title', 'id')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)
    # company = CompanySerializer(required=False)

    class Meta:
        model = Dish
        fields = '__all__'

    def create(self, validated_data):
        categories = validated_data.pop("categories", [])
        instance = Dish.objects.create(**validated_data)
        for category in categories:
            instance.categories.add(category)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        categories = validated_data.pop("categories", [])
        instance = super().update(instance, validated_data)
        for category in categories:
            instance.categories.add(category)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CartContentSerializer(serializers.ModelSerializer):
    product = DishSerializer()

    class Meta:
        model = CartContent
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer
    cart_content = CartContentSerializer(source='get_cart_content', many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_content')
        depth = 1
