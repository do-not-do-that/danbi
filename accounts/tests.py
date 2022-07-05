import json
from django.contrib.auth import get_user_model, authenticate
from django.test import (
    TestCase,
    Client
)


client = Client()


class SignupTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        get_user_model().objects.all().delete()

    def test_signup_post_success(self):
        sign_up_info = {
            "email" : "test58@test.com",
            "password1" : "wjdqhqhdks12!",
            "password2" : "wjdqhqhdks12!"
        }

        response=client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_signup_post_invalid_email(self):
        sign_up_info = {
            "email" : "test55test.com",
            "password1" : "wjdqh12!",
            "password2" : "wjdqh12!"
        }

        response=client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "email" : ["Enter a valid email address."]
        })

    def test_signup_post_invalid_password_not_exist_number(self):
        sign_up_info = {
            "email" : "test55@test.com",
            "password1" : "wjdqhqhdks!",
            "password2" : "wjdqhqhdks!"
        }

        response=client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "password1" : ["The password must contain at least 1 digit, 0-9."]
        })

    def test_signup_post_invalid_password_not_exist_symbol(self):
        sign_up_info = {
            "email" : "test55@test.com",
            "password1" : "wjdqhqhdks12",
            "password2" : "wjdqhqhdks12"
        }

        response=client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "password1" : ["The password must contain at least 1 symbol: ()[]{}|\\`~!@#$%^&*_-+=;:'\",<>./?"]
        })

    def test_signup_post_invalid_password_not_equal_pw(self):
        sign_up_info = {
            "email" : "test55@test.com",
            "password1" : "wjdqhqhdks12!",
            "password2" : "wjdqhqhdks12"
        }

        response=client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "non_field_errors" : ["The two password fields didn't match."]
        })


class LoginLogoutTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='testtest123!')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_correct(self):
        user = authenticate(email='test@example.com', password='testtest123!')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_login_wrong_email(self):
        user = authenticate(email='worng@example.com', password='testtest123!')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_wrong_password(self):
        user = authenticate(email='test@example.com', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


        