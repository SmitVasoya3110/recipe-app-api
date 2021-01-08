from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'smit@gmail.com'
        password = 'smit88665'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        # self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """TEST the email for a new user is normalized"""
        email = 'smit12@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_user_valid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_super_user(self):

        user = get_user_model().objects.create_superuser(
            'smit1@gmail.com',
            'admin1234'
        )

        self.assertTrue(user.is_superuser)
