from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainSlidingView

from . import models, serializers
from .pagination import AnnouncementPagination
from .permissions import AnnouncementPermission


class AuthView(TokenObtainSlidingView):
    """Авторизация пользователя"""

    serializer_class = serializers.AuthSerializer
    permission_classes = (AllowAny,)


class UserCreateView(generics.CreateAPIView):
    """Регистрация пользователя"""

    queryset = models.User
    serializer_class = serializers.UserCreateSerializer
    permission_classes = (AllowAny,)


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    create:
    Создание объявления

    retrieve:
    Получение объявления по идентификатору

    destroy:
    Удаление объявления

    list:
    Получение списка всех объявлений
    """

    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer
    permission_classes = (AnnouncementPermission,)
    pagination_class = AnnouncementPagination

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BaseAnnouncementUserListView(generics.ListAPIView):
    """Base announcement user view to extend in subclasses."""

    serializer_class = serializers.AnnouncementSerializer
    permission_classes = (AllowAny,)
    pagination_class = AnnouncementPagination
    lookup_field = "user_id"


class UserAnnouncementsListView(BaseAnnouncementUserListView):
    """Получение списка объявлений принадлежащих пользователю с указанным user_id"""

    def get_queryset(self):
        return models.Announcement.objects.filter(
            user_id=self.kwargs.get(self.lookup_field)
        )


class FeedForUserListView(BaseAnnouncementUserListView):
    """Получение ленты объявлений для пользователя с указанным user_id"""

    def get_queryset(self):
        return models.Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_field)
        )


class BaseMapListView(generics.ListAPIView):
    """Base announcements map view to extend in subclasses."""

    serializer_class = serializers.AnnouncementsMapSerializer
    permission_classes = (AllowAny,)


class MapListView(BaseMapListView):
    """Получение всей карты объявлений"""

    queryset = models.Announcement.objects.all()


class MapForUserListView(BaseMapListView):
    """Получение карты объявлений из ленты для пользователя с указанным user_id"""

    lookup_field = "user_id"

    def get_queryset(self):
        return models.Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_field)
        )
