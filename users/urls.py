from django.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import SignInAPIView
from .views import SignOutAPIView
from .views import SignUpAPIView

auth_urls = [
    path("signup/", SignUpAPIView.as_view(), name="sign-up"),
    path("signin/", SignInAPIView.as_view(), name="sign-in"),
    path("signout/", SignOutAPIView.as_view(), name="sign-out"),
]

token_urls = [path("refresh/", TokenRefreshView.as_view(), name="refresh")]

urlpatterns = [path("auth/", include(auth_urls)), path("token/", include(token_urls))]
