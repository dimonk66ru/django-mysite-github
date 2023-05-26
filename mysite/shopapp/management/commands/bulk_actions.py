from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from shopapp.models import Order, Product
from typing import Sequence


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo bulk actions")

        result = Product.objects.filter(
            name__contains="Bread",
        ).update(discount=10)

        print(result)

        # info = [
        #     ("bread_1", 19),
        #     ("bread_2", 29),
        #     ("bread_3", 39),
        # ]
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        #
        # result = Product.objects.bulk_create(products)
        #
        # for obj in result:
        #     print(obj)

        self.stdout.write("Done")
