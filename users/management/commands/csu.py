from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='adminov@sky.pro',
            first_name='Admin',
            last_name='Adminov',
            birth_day='1990-10-10',
            role='admin',
            is_active=True,

        )
        user.set_password('adminov12345')
        user.save()
