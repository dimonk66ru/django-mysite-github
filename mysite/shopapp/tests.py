from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User, Permission
from random import choices
from shopapp.models import Product, Order
from shopapp.utils import add_two_numbers
from string import ascii_letters


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_superuser(username="admin", password="23")
        cls.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=cls.product_name).delete()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client = Client(HTTP_USER_AGENT="Mozilla")
        self.client.force_login(self.user)

    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123",
                "description": "A good table",
                "discount": "10",
                "created_by": self.user.pk,
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")
        self.user = User.objects.create_superuser(username="admin", password="23")
        self.product = Product.objects.create(name="Best Product", created_by=self.user, created_by_id=self.user.pk)
        self.client.force_login(self.user)

    def tearDown(self):
        self.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse("shopapp:products_details", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shopapp:products_details", kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
        'auth-fixture.json',
    ]

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")

    # def test_products(self):
    #     response = self.client.get(reverse("shopapp:products_list"))
    #     for product in Product.objects.filter(archived=False).all():
    #         self.assertContains(response, product.name)

    # def test_products(self):
    #     response = self.client.get(reverse("shopapp:products_list"))
    #     products = Product.objects.filter(archived=False).all()
    #     products_ = response.context["products"]
    #     for p, p_ in zip(products, products_):
    #         self.assertEqual(p.pk, p_.pk)

    def test_products(self):
        response = self.client.get(reverse("shopapp:products_list"))
        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="admin", password="23")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse("shopapp:orders_list"))
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:orders_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
        'auth-fixture.json',
    ]

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:products-export"),
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": str(product.price),
                "archived": product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data,
        )


class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="admin", password="23")
        perm = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(perm)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            user_id=self.user.pk,
            delivery_address="ul. Lenina 25-213",
            promocode="sale123"
        )

    def tearDown(self):
        self.order.delete()

    def test_order_details(self):
        response = self.client.get(
            reverse("shopapp:order_detail", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertContains(response, self.order.pk)


class OrderExportTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
        'auth-fixture.json',
        'orders-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="admin", password="23", is_staff="1")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT="Mozilla")
        self.client.force_login(self.user)

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:orders-export"),
        )
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user.pk,
                "products": order.products,
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(
            orders_data["orders"],
            expected_data,
        )
