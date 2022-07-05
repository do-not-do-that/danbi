import json
from rest_framework.test import APITestCase
from rest_framework.views import status
from django.contrib.auth import get_user_model


class RoutineTest(APITestCase):
    def setUp(self):
        self.url = '/routines/'
        sign_up_info = {
            "email" : "test58@test.com",
            "password1" : "wjdqhqhdks12!",
            "password2" : "wjdqhqhdks12!"
        }

        self.response=self.client.post('/accounts/', json.dumps(sign_up_info), content_type='application/json')


    def test_routine_post_data(self):
        data = {
            "title": "테스트 타이틀",
            "days": ["SUN"],
            "goal": "테스트 goal",
            "category": "HOMEWORK",
            "is_alarm": "true"
        }
        response = self.client.post(self.url, data=data, format='json',  **{'HTTP_AUTHORIZATION': self.response.content})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)