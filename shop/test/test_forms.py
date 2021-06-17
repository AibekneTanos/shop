from django.test import TestCase

from shop.forms import RegisterForm, LoginForm


class RegisterFormTest(TestCase):
    def test_email_fail(self):
        form_data = {
            "username": "test_username",
            'email': '@gmail.comasdasdasddasdx.,a,sdw',
            'password1': "testpassword121212",
            'password2': "testpassword121212"

        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_email_fail_s(self):
        form_data = {
            "username": "test_username",
            'email': 'nicemoonmoonice@gmailcom',
            'password1': "testpassword121212",
            'password2': "testpassword121212"

        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_email_(self):
        form_data = {
            'username': 'test_username',
            'email': 'nicemoonmoonice@gmail.com',
            'password1': "testpassword121212",
            'password2': "testpassword121212"

        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())


class LoginFormTest(TestCase):
    def test_login(self):
        from_data = {
            'login': 'WhereImGoingWait7',
            'password': 'qwe12345678'
        }
        form = LoginForm(data=from_data)
        self.assertTrue(form.is_valid())

    def test_login_fail(self):
        from_data = {
            'login': 'WhereImGoindWait7' * 25,
            'password': 'qwe123456789'
        }
        form = LoginForm(data=from_data)
        self.assertFalse(form.is_valid())

