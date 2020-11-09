from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from firebase_admin import auth
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from .serializers import LoginSocialSerializer
from .models import User
from .serializers import UserSerializer,UserPagination

import datetime
import pytz
from django.utils import timezone

class UserListApiView(ListAPIView):
    serializer_class = UserSerializer
    pagination_class = UserPagination
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all().order_by('-last_login')

class LoginUser(TemplateView):
    template_name = "users/login.html"

class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        id_token = serializer.data.get('token_id')
        decode_token = auth.verify_id_token(id_token)

        email = decode_token['email']
        name = decode_token['name']
        avatar = decode_token['picture']
        verified = decode_token['email_verified']

        usuario, created = User.objects.get_or_create(
            email = email,
            defaults={
                'full_name' : name,
                'email' : email,
                'is_active': True
            }
        )
        tz_CO = pytz.timezone('America/Bogota') 
        datetime_CO = datetime.datetime.now(tz_CO)
        

        usuario.last_login = datetime_CO
        usuario.save()

        if created:
            token = Token.objects.create(user = usuario)
        else:
            token = Token.objects.get(user = usuario)
        userGet = {
            'id': usuario.pk,
            'email': usuario.email,
            'full_name': usuario.full_name,
            'last_login': usuario.last_login
        }

        return Response(
            {
                'token': token.key,
                'user': userGet
            }
        )