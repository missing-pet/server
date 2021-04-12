"""Test cases for serializers."""
from django import test

from .. import serializers
from .data_factories import UserFactory


class SerializerTestCase(test.TestCase):
    def setUp(self):
        pass

    def test_user_create_serializer(self):
        data = {
            'email': 'test@email.com',
            'nickname': 'nickname',
            'password': 'Password123*',
        }

        serializer = serializers.UserCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        data2 = {
            'email': 'abcde',
            'nickname': 'nickname',
            'password': 'Password123*',
        }

        serializer = serializers.UserCreateSerializer(data=data2)
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_password_reset_request_serializer(self):
        user = UserFactory(email='email@mail.ru')

        data = {
            'email': user.email,
        }
        serializer = serializers.PasswordResetRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def tearDown(self):
        pass
