from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    """
    Creates order
    """
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="ul Lenina dom 18",
            promocode='SALE',
            user=user,
        )
        self.stdout.write(f"Created order {order}")

        order = Order.objects.first()
        products = Product.objects.all()
        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added products{order.products.all()} to order {order}"
            )
        )
