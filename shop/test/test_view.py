from django.contrib.auth.models import User
from django.test import TestCase
from shop import views
from django.urls import reverse


class TestHomePageViews(TestCase):
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'index.html')


class TestRegisterPageView(TestCase):
    def test_register(self):
        response = self.client.get(reverse('registr'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'registr.html')


class TestEditViewPage(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='TsetUser', password='OdinNotLoki123')

    def test_edit(self):
        self.client.login(username='TsetUser', password='OdinNotLoki123')
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'edit.html')


class TestCartViewPage(TestCase):
    def test_cart(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'cart.html')


class TestLoginViewPage(TestCase):
    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'login.html')
