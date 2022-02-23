from rest_framework.serializers import ModelSerializer
from .models import Author, Our_user


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = Our_user
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]