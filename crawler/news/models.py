from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name='Заголовок',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    url = models.URLField(
        verbose_name='URL новости',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

