from django.urls import include, path
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_shop.urls import router
from shop.models import Company




class AccountTests(APITestCase):
    urlpatterns = [
        path('', include(router.urls)),
    ]

    def setUp(self):
        User.objects.create_superuser(username='momoshiki', password='otsusuki2004')
        self.company = Company.objects.create(title='ZaDanbas')



    def test_apicompanies_account(self):
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


    def test_put_company(self):
        self.client.login(username='momoshiki', password='otsusuki2004')
        data = {
            'title': 'test_title'
        }
        request = self.client.patch("/api/companies/1/", data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.title, data['title'])

