from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Product, Order

class Command(BaseCommand):
    """
    Создание новых заказа
    """

    def handle(self, *args, **options):
        self.stdout.write('Создаем заказ')
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_adress='ул. Ленина д. 7',
            promocode='SALE',
            user=user,
        )
        self.stdout.write(f'Созданный заказ {order}')
