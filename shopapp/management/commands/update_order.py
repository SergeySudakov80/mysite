from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write('Заказ не найден')
            return
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()

        self.stdout.write(
            self.style.SUCCESS(f'Успешное добавление продуктов: {order.products.all()} в заказ {order}')
        )
