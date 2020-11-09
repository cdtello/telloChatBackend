from django.db.models import fields
from django.utils.translation import activate
from rest_framework import serializers, pagination
from .models import Message 

from applications.users.serializers import UserSerializer





class MessageSerializer(serializers.ModelSerializer):

    # aditionals = serializers.type(default=false)
    # si es many to many se pone (many=true) 
    # author = UserSerializer() 
    class Meta:
        model = Message
        # fields = ('__all__')
        fields = (
            'id',
            'message',
            'image',
            'author',
            'active',
            'created',
            'modified',
        )

    # ******** Custom Serializer **********
# class MessageSerializerSimple(serializers.Serializer):
#     id = serializers.IntegerField()
#     message = serializers.CharField()
#     image = serializers.CharField()
#     author = serializers.IntegerField()
#     active = serializers.BooleanField(default = true) (required = false)


class MessagePagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 100
    
