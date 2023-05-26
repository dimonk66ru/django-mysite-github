from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from shopapp.models import Order, Product
from typing import Sequence


class Command(BaseCommand):
    """
    Creates order
    """
    @transaction.atomic
    def handle(self, *args, **options):
        # with transaction.atomic():
        #     ...
        self.stdout.write("Create order with products")
        user = User.objects.get(username="admin")
        # products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()
        products: Sequence[Product] = Product.objects.only("id").all()
        order, created = Order.objects.get_or_create(
            delivery_address="ul Lenina dom 18",
            promocode="SALE",
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f"Created order {order}")

