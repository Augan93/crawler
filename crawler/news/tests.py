from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import News


class CreateBlogTest(APITestCase):
    """Тест Создание поста"""
    def setUp(self):
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

    def test_invalid_sort_param(self):
        url = reverse('news:news_list')
        print(url)
        response = self.client.get(url + '?sort={}'.format('4ASDid'))

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)


    # def test_create_blog_by_common_user(self):
    #     """Создание поста как обычный пользователь (НЕ БЛОГ-АДМИН)"""
    #     self.superuser = User.objects.create_superuser(
    #         username='test@mail.ru',
    #         email='test@mail.ru',
    #         password='123'
    #     )
    #     self.profile = Profile.objects.create(
    #         user=self.superuser,
    #         middle_name='middleName',
    #         first_name='firstName',
    #         last_name='lastName',
    #         phone='phone',
    #         self_registration=True,
    #         confirm_id=str(uuid4()),
    #         uid1c=str(uuid4()),
    #         connect_token=str(uuid4()),
    #         blog_admin=False,
    #     )
    #     self.client.login(username='test@mail.ru',
    #                       password='123')
    #
    #     url = reverse('blog:post-create')
    #     response = self.client.post(url,
    #                                 self.data,
    #                                 format='json')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    #
