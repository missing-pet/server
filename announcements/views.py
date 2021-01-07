from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Announcement
from .permissions import IsAnnouncementAuthorOrReadOnly
from .serializers import AnnouncementListCreateSerializer
from .serializers import AnnouncementRetrieveSerializer
from .serializers import AnnouncementsMapListSerializer


class AnnouncementListCreateAPIView(ListCreateAPIView):
    """Список всех объявлений/Создание объявления."""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AnnouncementRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """Получение/удаление объявления."""

    queryset = Announcement
    serializer_class = AnnouncementRetrieveSerializer
    permission_classes = (IsAnnouncementAuthorOrReadOnly, )


class UserAnnouncementsListAPIView(ListAPIView):
    """Объявления пользователя с указанным user_id."""

    serializer_class = AnnouncementRetrieveSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return Announcement.objects.filter(
            user_id=self.kwargs.get(self.lookup_url_kwarg))


class FeedForUserListAPIView(ListAPIView):
    """Лента объявлений для пользователя с указанным user_id."""

    serializer_class = AnnouncementRetrieveSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_url_kwarg))


class AnnouncementsMapListAPIView(ListAPIView):
    """Карта всех объявлений."""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementsMapListSerializer
    pagination_class = None


class AnnouncementsMapForUserListAPIView(ListAPIView):
    """
    Карта объявлений \
    (без объявлений, созданных пользователем с указанным user_id).
    """

    serializer_class = AnnouncementsMapListSerializer
    pagination_class = None
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return Announcement.objects.exclude(
            user_id=self.kwargs.get(self.lookup_url_kwarg))
