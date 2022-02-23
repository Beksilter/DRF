import json
import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError
from library.models import Our_user


class Command(BaseCommand):
    USER_DATA_FILE = os.path.join(
        settings.BASE_DIR,
        'library/management/data/users_samples.json'
    )

    def handle(self, *args, **options):
        print('_______________START_______________')

        try:
            Our_user.objects.create_superuser(
                username=settings.SUPERUSER_NAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD,
                first_name=settings.SUPERUSER_FIRST_NAME,
                last_name=settings.SUPERUSER_LAST_NAME,
            )
            print(f'New SuperUser {settings.SUPERUSER_NAME} created!')
        except IntegrityError:
            print(f'ERROR: SuperUser {settings.SUPERUSER_NAME} '
                  f' already exists!')

        with open(self.USER_DATA_FILE) as f:
            users = json.load(f)

        for user in users:
            if not Our_user.objects.filter(**user):
                Our_user.objects.create(**user)
                print(f'User {user["username"]} created')
            else:
                print(f'ERROR: User {user["username"]} '
                      f'already exists')

        print('_______________FINISH_______________')