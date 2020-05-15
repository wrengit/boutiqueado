from django.test import TestCase
from .models import Product


class TestViews(TestCase):
    def test_all_products_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_product_detail_page(self):
        product = Product.objects.create(name="Test Product", price=5.55)
        response = self.client.get(f"/products/{product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
