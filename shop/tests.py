from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Category
from .models import Product
from django.forms import DecimalField
from decimal import Decimal

class shoptest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email='test@email.com',
            password = 'secret',
        )

        self.category = Category.objects.create(
            name='A name',
            description='Description',
            image='An image',
        )

        self.product = Product.objects.create(
            name = 'A name',
            description = 'Description',
            category = self.category,
            price = 0.00,
            image = 'An image',
            stock = 0,
            available = True,
            created = 'Date created',
            updated = 'Date Updated',
        )

    def test_string_representation(self):
        category = Category(name='A name')
        self.assertEqual(str(category), category.name)
        product = Product(name='A name')
        self.assertEqual(str(product), product.name)

    def test_category_content(self):
        self.assertEqual(f'{self.category.name}', 'A name')
        self.assertEqual(f'{self.category.description}', 'Description')
        self.assertEqual(f'{self.category.image}', 'An image') 

    def test_product_content(self):
        self.assertEqual(f'{self.product.name}', 'A name')
        self.assertEqual(f'{self.product.description}', 'Description')
        self.assertEqual(f'{self.product.category}', 'Category')
        self.assertEqual(f'{self.product.price}', Decimal)
        self.assertEqual(f'{self.product.image}', 'An image')
        self.assertEqual(f'{self.product.stock}', 'amount in stock')
        self.assertEqual(f'{self.product.available}', bool)
        self.assertEqual(f'{self.product.created}', 'Date created')
        self.assertEqual(f'{self.product.updated}', 'Date Updated')

    def test_category_list_view(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body content')
        self.assertTemplateUsed(response, 'base.html')


    def test_product_list_view(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body content')
        self.assertTemplateUsed(response, 'base.html')

    def test_category_detail_view(self):
        response = self.client.get('/category/1/')
        no_response = self.client.get('/category/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A name')
        self.assertTemplateUsed(response, 'products_by_category.html')

    def test_product_detail_view(self):
        response = self.client.get('/product/1/')
        no_response = self.client.get('/product/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A name')
        self.assertTemplateUsed(response, 'prod_detail.html')