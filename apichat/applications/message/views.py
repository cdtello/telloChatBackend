from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import ListView

from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Message 

from .serializers import MessageSerializer, MessagePagination

class ListMessages(ListView):
    template_name = "message/messages.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.all()

# Utilizando RestFramework

class MessageListApiView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = MessagePagination

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.all()

class MessageSearchApiView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = MessagePagination

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Message.objects.filter(
            message__icontains = kword
        )

class MessageCreateView(CreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = MessageSerializer

class MessageDetailView(RetrieveAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class MessageDeleteView(DestroyAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

# class MessageUpdateView(UpdateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

class MessageUpdateView(RetrieveUpdateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

