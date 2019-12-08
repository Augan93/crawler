from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import News
import json


class CreateBlogTest(APITestCase):
    """Тест Создание поста"""

    def setUp(self):
        self.url = reverse('news:news_list')
        self.data = [
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },
            {
                'title': 'Test',
                'url': 'asdas',
            },

        ]
        for item in self.data:
            News.objects.create(**item)

    def test_invalid_order_param(self):
        response = self.client.get(self.url,
                                   data={'order': 'idad'})

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_asc_order_by_id(self):
        """Тест сортировки по возрастанию id"""
        response = self.client.get(self.url,
                                   data={'order': 'id'})
        news = json.loads(response.content)
        sorted_news = sorted(news,
                             key=lambda item: item['id'])
        self.assertEqual(news,
                         sorted_news)

    def test_desc_order_by_id(self):
        """Тест сортировки по убыванию id"""
        response = self.client.get(self.url,
                                   data={'order': '-id'})
        news = json.loads(response.content)
        sorted_news = sorted(news,
                             key=lambda item: item['id'],
                             reverse=True)

        self.assertEqual(news,
                         sorted_news)

    def test_order_offset_limit_by_id(self):
        """Тест сортировки по возрастанию id, offset=2, limit=4"""
        response = self.client.get(self.url,
                                   data={
                                       'order': 'id',
                                       'offset': '2',
                                       'limit': '4'})
        news = json.loads(response.content)
        sorted_news = sorted(news,
                             key=lambda item: item['id'])
        print(news)
        print(sorted_news)

        self.assertEqual(news,
                         sorted_news)
        self.assertEqual(len(news),
                         4)

    def test_news_count(self):
        """Тест количество возвращаемых постов (по умполчанию - 5)"""
        response = self.client.get(self.url,
                                   data={'order': 'id'})

        news = json.loads(response.content)

        self.assertEqual(len(news),
                         5)

    def test_news_limit(self):
        """Тест limit постов"""
        response = self.client.get(self.url,
                                   data={'limit': '3'})

        news = json.loads(response.content)

        self.assertEqual(len(news),
                         3)

    def test_negative_limit(self):
        """Тест, минусовой параметр limit"""
        response = self.client.get(self.url,
                                   data={'limit': '-3'})
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "negative_limit_is_not_allowed")

    def test_negative_offset(self):
        """Тест, минусовой параметр offset"""
        response = self.client.get(self.url,
                                   data={'offset': '-3'})
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "negative_offset_is_not_allowed")

    def test_negative_limit_or_offset(self):
        """Тест, минусовой параметр offset и limit"""
        response = self.client.get(self.url,
                                   data={
                                       'offset': '-3',
                                       'limit': '-3',
                                   })
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "negative_limit_or_offset_is_not_allowed")

    def test_non_numeric_limit(self):
        """Тест не числовой параметр limit"""
        response = self.client.get(self.url,
                                   data={'limit': 'adad'})
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "invalid_param")

    def test_non_numeric_offset(self):
        """Тест не числовой параметр offset"""
        response = self.client.get(self.url,
                                   data={'offset': 'adad'})
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "invalid_param")

    def test_non_numeric_limit_or_offset(self):
        """Тест не числовой параметр offset и limit"""
        response = self.client.get(self.url,
                                   data={
                                       'offset': 'adad',
                                       'limit': '3asd',
                                   })
        message = json.loads(response.content)

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message['message'], "invalid_param")
