from django.contrib.auth.models import User
from django.test import TestCase
from shop.models import Category, Company, Dish, Location, UserProfile, Kit, Cart, CartContent


class TestDish(TestCase):
    def setUp(self):
        self.cot = Category.objects.create()
        self.comp = Company.objects.first()
        self.payload = {
            'title': 'title',
            'dish_type': 'dish_type',
            'image': 'img.jpg',
            'description': 'descriptions',
            'company': self.comp,
            'price': 200
        }

    def test_dish_create(self):
        dish = Dish.objects.create(**self.payload)
        dish.categories.add(self.cot)
        dish.save()
        self.assertEqual(dish.title, self.payload['title'])

    def test_update_dish(self):
        new_title = 'new_title'
        dish = Dish.objects.create(**self.payload)
        dish.categories.add(self.cot)
        dish.title = new_title
        dish.save()
        dish.refresh_from_db()
        self.assertEqual(dish.title, new_title)

    def test_dish_delete(self):
        dish = Dish.objects.create(**self.payload)
        dish.categories.add(self.cot)
        pk = dish.pk
        dish.delete()
        with self.assertRaises(Dish.DoesNotExist):
            dish = Dish.objects.get(pk=pk)


class TestCategory(TestCase):
    def test_create_category_success(self):
        payload = {
            'title': 'test_title',
            'description': 'test_description'
        }
        category = Category.objects.create(**payload)
        self.assertEqual(category.title, payload['title'])

    def test_category_update(self):
        new_title = 'new_title'
        payload = {
            'title': 'test_title',
            'description': 'test_description'
        }
        category = Category.objects.create(**payload)
        category.title = new_title
        category.save()
        self.assertEqual(category.title, new_title)

    def test_category_delete(self):
        payload = {
            'title': 'test_title',
            'description': 'test_description'
        }
        category = Category.objects.create(**payload)
        pk = category.pk
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            category = Category.objects.get(pk=pk)


class TestCompany(TestCase):
    def test_create(self):
        payload = {
             'title': 'test_title'
        }
        company = Company.objects.create(**payload)
        self.assertEqual(company.title, payload['title'])

    def test_update_company(self):

        new_title ='new_test_title'
        payload = {
            'title': "test_title"
        }

        category = Category.objects.create(**payload)

        category.title = new_title
        category.save()
        self.assertEqual(category.title, new_title)

    def test_company_delete(self):
        payload = {
            'title': 'test_title',
        }
        company = Company.objects.create(**payload)
        pk = company.pk
        company.delete()
        with self.assertRaises(Company.DoesNotExist):
            company = Company.objects.get(pk=pk)


class TestLocation(TestCase):
    def setUp(self):
        self.payload = {
            'country': 'test_country'
        }

    def test_loc_create(self):
        loc = Location.objects.create(**self.payload)
        loc.save()
        self.assertEqual(loc.country, self.payload['country'])

    def test_loc_update(self):
        new_country = 'new_country'
        loc = Location.objects.create(**self.payload)
        loc.country = new_country
        loc.save()
        self.assertEqual(loc.country, new_country)

    def test_loc_delete(self):
        loc = Location.objects.create(**self.payload)
        pk = loc.pk
        loc.delete()
        with self.assertRaises(Location.DoesNotExist):
            loc = Location.objects.get(pk=pk)


class TestCart(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='zefit', password='oladyk123456')

    def test_cart_create(self):
        payload = {
            'user': self.user,
            'total_cost': 222
        }
        cart = Cart.objects.create(**payload)
        cart.save()
        self.assertEqual(cart.total_cost, 222)

    def test_cart_update(self):
        new_cost = 2222
        payload = {
            'user': self.user,
            'total_cost': 22
        }
        cart = Cart.objects.create(**payload)
        cart.total_cost = new_cost
        cart.save()
        self.assertEqual(cart.total_cost, new_cost)

    def test_cart_delete(self):
        payload = {
            'user': self.user,
            'total_cost': 222
        }
        cart = Cart.objects.create(**payload)
        pk = cart.pk
        cart.delete()
        with self.assertRaises(Cart.DoesNotExist):
            cart = Cart.objects.get(pk=pk)


class TestCartContent(TestCase):
    def setUp(self):
        self.category = Category.objects.create()
        self.company = Company.objects.first()
        self.user = User.objects.create_user(username='zefit', password='oladyk123456')
        self.data = {
            'title': 'test_title',
            'dish_type': 'test_dish_type',
            'description': 'test_description',
            'company': self.company,
            'price': 222
        }
        self.dish = Dish.objects.create(**self.data)
        self.dish.categories.add(self.category)
        self.dish.save()

        self.payload = {
            'user': self.user,
            'total_cost': 222
        }
        self.cart = Cart.objects.create(**self.payload)

    def test_create(self):
        data = {
            'cart': self.cart,
            'product': self.dish,
            'qty': 222
        }
        cartContent = CartContent.objects.create(**data)
        self.assertEqual(cartContent.qty, 222)

    def test_update(self):
        new_qty = 111
        data = {
            'cart': self.cart,
            'product': self.dish,
            'qty': 222
        }
        cartContent = CartContent.objects.create(**data)
        cartContent.qty = new_qty
        self.assertEqual(cartContent.qty, new_qty)

    def test_delete(self):
        data = {
            'cart': self.cart,
            'product': self.dish,
            'qty': 222
        }
        cartContent = CartContent.objects.create(**data)
        pk = cartContent.pk
        cartContent.delete()
        with self.assertRaises(CartContent.DoesNotExist):
            cartContent = CartContent.objects.get(pk=pk)


