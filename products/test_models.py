from django.test import TestCase
from .models import Product, Category


class TestModels(TestCase):
    def test_product_name_returns_self_name(self):
        product = Product.objects.create(name="Test Product", price=1.11)
        self.assertEqual(str(product), "Test Product")

    def test_category_name_returns_self_name(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")

    def test_category_friendly_name_returns_friendly_name(self):
        category = Category.objects.create(name = "Test Category", friendly_name="Category Friendly Name")
        self.assertEqual(category.get_friendly_name(), "Category Friendly Name")
