from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """
    Создание новых продуктов
    """

    def handle(self, *args, **options):
        self.stdout.write('Создание продуктов')

        products_names = [
            'Laptop',
            'Desctop',
            'Smartphon'
        ]
        for product_name in products_names:
            product, create = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f'Создан продукт {product_name}')

        self.stdout.write(self.style.SUCCESS('Продукты успешно созданы'))
