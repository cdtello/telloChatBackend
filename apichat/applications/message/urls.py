from django.urls import path, re_path

from . import views

app_name = 'message_app'

urlpatterns = [
    path(
        'messages/',
        views.ListMessages.as_view(),
        name = 'messages'
    ),
    path(
        'api/message/list/',
        views.MessageListApiView.as_view(),
    ),
    path(
        'api/message/create/',
        views.MessageCreateView.as_view(),
    ),
    path(
        'api/message/detail/<pk>/',
        views.MessageDetailView.as_view(),
    ),
    path(
        'api/message/delete/<pk>/',
        views.MessageDeleteView.as_view(),
    ),
    path(
        'api/message/update/<pk>/',
        views.MessageUpdateView.as_view(),
    ),
    path(
        'api/message/search/<kword>/',
        views.MessageSearchApiView.as_view(),
    ),
    
]
