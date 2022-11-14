from django.test import TestCase
from django.test import Client

# Create your tests here.


class InventoryTestCase(TestCase):
    def setUp(self):
        # Create the client
        self.client = Client()

    def test_inventory_api_200(self):
        # Visit the inventory list page
        response = self.client.get('/inventory/api/inventory', follow=True)

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)

    def test_inventory_list_page_200(self):
        # Visit the inventory list page
        response = self.client.get('/inventory/')

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)

    def test_inventory_page_200(self):
        # Visit the inventory list page
        response = self.client.get('/inventory/')

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)
