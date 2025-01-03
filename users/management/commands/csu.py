from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя при запуске.
    """
    def handle(self, *args, **options):
        """
        Метод обработки команды. Создает нового суперпользователя с заданными параметрами.
        """

        user = User.objects.create(email="addmin@gmail.com")
        user.set_password("123qwerty")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
