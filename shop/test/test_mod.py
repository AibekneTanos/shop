from django.test import TestCase
from shop.models import Category, Company, Dish


class TstDish(TestCase):
    def test_title(self):
        cot = Category.objects.create()
        comp = Company.objects.first()
        payload = {
            'title': 'title',
            'dish_type': 'dish_type',
            'image': 'img.jpg',
            'description': 'descriptions',
            'company': comp,
            'price': 200
        }

        dish = Dish.objects.create(**payload)
        dish.categories.add(cot)
        self.assertEqual(dish.title, payload['title'])

class TestCategory(TestCase):
    def test_create_category_success(self):
        payload = {
            'title': 'test_title'
        }
        category = Category.objects.create(**payload)
        self.assertEqual(category.title, payload['title'])

class TestCompany(TestCase):
    def test_create(self):
        payload = {
             'title': 'test_title'
        }
        company = Company.objects.create(**payload)
        self.assertEqual(company.title, payload['title'])


    def test_create_fail(self):
        payload = {
             'title': 'test_title',
            'unknown_field': 'value'
        }
        with self.assertRaises(TypeError):
            Company.objects.create(**payload)


    def test_update_company(self):

        new_title ='new_test_title'
        payload = {
            'title': "test_title" * 25,
        }

        category = Category.objects.create(**payload)

        category.title = new_title
        category.save()



    def test_delete(self):
         payload ={
             'title': 'test_title',
         }
         company = Company.objects.create(**payload)
         pk = company.pk
         company.delete()
         with self.assertRaises(Company.DoesNotExist):
             company = Company.objects.get(pk=pk)


# class TestDish(TestCase):
# def test_dish_create (self):
#  comp = Company.objects.first()
# for index in comp:
# compindex

#    break()
# payload ={
# "image": "test_title",
# "title":'test_title',
# "dish_type":"test_dish_type",
# "descreption": "test_title",
# "categories": "test_title",
# "company": comp,
# "price": 100
# }
# Dish.objects.create(**payload)
# self.assertEqual(dish.)
