from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'login/',
        views.LoginUser.as_view(),
        name='Login'
    ),
    path(
        'api/google-login/',
        views.GoogleLoginView.as_view(),
        name='users-google_login'
    ),
    path(
        'api/user/list/',
        views.UserListApiView.as_view(),
    ),
]