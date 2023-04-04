from django.test import TestCase
from django.urls import reverse
from shopapp.utils import add_two_numbers



class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": "Table",
                "price": "123",
                "description": "A good table",
                "discount": "10",
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
