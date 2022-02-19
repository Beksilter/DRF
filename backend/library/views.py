from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorModelSerializer, UserModelSerializer
from .models import Author, Our_user


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = Our_user.objects.all()