from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser as User
import json


class IndexTestCase(APITestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CustomUserTestCase(APITestCase):   

    def setUp(self):
        self.user = User.objects.create(
            document_type="cedula",
            document="123asder2566",
            first_name="user",
            last_name="user",
            email="test@gmail.com",
            hobbie="test"
        )
        self.put_data = {
            'document_type': 'cedula',
            'document': '123asder2566',
            'first_name': 'user',
            'last_name': 'last name',
            'email': 'test@gmail.com',
            'hobbie': 'hobbie'
        }
        self.patch_data = {
            'document_type': 'passport'
        }

    def test_create_user(self):
        user = User.objects.get(document_type='cedula')        
        self.assertEqual(user.email,'test@gmail.com')
        
    def test_pacth_user(self):
        response = self.client.patch(
            reverse('user_detail', kwargs={'pk': self.user.pk}),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        response = self.client.patch(
            reverse('user_detail', kwargs={'pk': self.user.pk}),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.delete(
            reverse('user_detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

