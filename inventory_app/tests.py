from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item  # Import your Item model
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


class ItemTests(APITestCase):
    
    def setUp(self):
        # Create an item for testing
       
        self.user = User.objects.create_user(username='inventory', password='inventory')
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        self.item = Item.objects.create(name='Test Item', description='This is a test item.')

    def test_create_item(self):
        url = reverse('items') 
        data = {'name': 'New Item', 'description': 'Description of new item.'}
        count = Item.objects.count()
        response = self.client.post(url, data, format='json')
       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), count+1)  # To check the item count increased 0r not
        self.assertEqual(Item.objects.get(id=response.data['id']).name, 'New Item')

    def test_read_item(self):
        url = reverse('items', args=[self.item.id])  # URL to read an item
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        url = reverse('items', args=[self.item.id])  # URL to update the item
        data = {'name': 'Updated Item', 'description': 'Updated description.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()  # Refresh the item from the database
        self.assertEqual(self.item.name, 'Updated Item')

    def test_delete_item(self):
        url = reverse('items', args=[self.item.id])  # URL to delete the item
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)  # Check if the item was deleted
