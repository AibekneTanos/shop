from django.contrib.auth.models import User, Group
from rest_framework import serializers
from shop.models import Dish, Cart, Company, Category, CartContent


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ['id', 'title']




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['title']





class DishSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)
    # company = CompanySerializer(required=False)
    depth = 2

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
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class CartContentSerializer(serializers.ModelSerializer):
    product = DishSerializer()


    class Meta:
        model = CartContent
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer
    #cart_content = CartContentSerializer(source='get_cart_content', many=True)
    depth = 1

    class Meta:
        model = Cart
        fields = ('id', 'user', 'session_key')

    def create(self, validated_data):
        carts = validated_data.pop('carts', [])
        instance = Cart.objects.create(**validated_data)
        for carts in Cart:
            instance.carts.add(cart_content)
        instance.save()
        return instance