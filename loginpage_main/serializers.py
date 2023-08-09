from .models import Home
from rest_framework import serializers

class Home_get_serializer(serializers.ModelSerializer):
    class Meta:
        model= Home
        fields = "__all__"

class Home_post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"

class Home_put_serializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"