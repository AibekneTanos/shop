from django.urls import include, path
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_shop.urls import router
from shop.models import Company, Dish, Category


class UsersTests(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='Fenrir', password='json123')
        data = {
            'username': 'testName',
            'password': 'kuku123'
        }
        user = self.client.post('/api/users/', data, format='json')

    def test_user_create(self):
        self.client.login(username='Fenrir', password='json123')
        data = {
            'username': 'testName',
            'password': 'kuku123'
        }
        user = self.client.post('/api/users/', data, format='json')
        self.assertEqual(user.status_code, 201)

    def test_user_patch(self):
        self.client.login(username='Fenrir', password='json123')
        data = {
            'username': 'New_Name'
        }
        user = self.client.patch('/api/users/1/', data, format='json')
        self.assertEqual(User.objects.all().first().username, data['username'])

    def test_user_put(self):
        self.client.login(username='Fenrir', password='json123')
        data = {
            'username': 'New_Name',
            'password': 'newpassword123'
        }
        user = self.client.patch('/api/users/1/', data, format='json')
        self.assertEqual(User.objects.all().first().password, data['password'])


class DishTests(APITestCase):

    urlpatterns = [
        path('', include(router.urls))
    ]

    def setUp(self):
        User.objects.create_superuser(username='momoshiki', password='empty000')
        self.company = Company.objects.create(title='test_title')
        self.categories = Category.objects.create(title='ZaDandas')

        self.client.login(username='momoshiki', password='empty000')
        data = {
            'title': 'test_title',
            'dish_type': 'test_dish_type',
            'company': self.company.id,
            'categories': [self.categories.id],
            'description': 'test_description',
            'price': 1000
        }
        self.dish = self.client.post('/api/dishes/', data, format='json')

    def test_dish_create(self):
        url = '/api/dishes/'
        self.client.login(username='momoshiki', password='empty000')
        data = {
            'title': 'test_title',
            'dish_type': 'test_dish_type',
            'company': self.company.id,
            'categories': [self.categories.id],
            'description': 'test_description',
            'price': 1000
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dish_patch(self):
        self.client.login(username='momoshiki', password='empty000')
        data = {
            'title': 'testButNewTitle',
        }
        response = self.client.patch('/api/dishes/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dish.objects.all().first().title, data['title'])

    def test_dish_put(self):
        self.client.login(username='momoshiki', password='empty000')
        data = {
            'title': 'testButNewTitle',
            'dish_type': 'newDishType',
            'company': self.company.id,
            'categories': [self.categories.id],
            'description': 'NewDes',
            'price': 2000
        }

        response = self.client.put('/api/dishes/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dish.objects.all().first().title, data['title'])


class CompanyTests(APITestCase):
    urlpatterns = [
        path('', include(router.urls)),
    ]

    def setUp(self):
        User.objects.create_superuser(username='momoshiki', password='otsusuki2004')
        self.company = Company.objects.create(title='ZaDanbas')

    def test_api_companies_account(self):
        self.client.login(username='momoshiki', password='otsusuki2004')
        url = '/api/companies/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_company(self):
        self.client.login(username='momoshiki', password='otsusuki2004')
        url = '/api/companies/'
        data = {
            'title': 'ZaDanbas'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.all().first().title, data['title'])

    def test_patch_company(self):
        self.client.login(username='momoshiki', password='otsusuki2004')
        data = {
            'title': 'test_title'
        }
        request = self.client.patch('/api/companies/1/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(Company.objects.all().first().title, data['title'])

    def test_put_company(self):
        self.client.login(username='momoshiki', password='otsusuki2004')
        data = {
            'title': 'new_title'
        }
        request = self.client.put('/api/companies/1/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(Company.objects.all().first().title, data['title'])

