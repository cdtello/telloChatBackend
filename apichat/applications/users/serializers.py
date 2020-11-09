from rest_framework import serializers, pagination
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

class LoginSocialSerializer(serializers.Serializer):
    token_id = serializers.CharField(required=True);
