from django.db import models

from conf import settings


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    preview = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='привью')
    description = models.TextField(**NULLABLE, verbose_name='описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='пользователь')

    class Meta:
        verbose_name ='курс'
        verbose_name_plural = 'курсы'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='курс', related_name='lesson')
    title = models.CharField(max_length=150, verbose_name='урок')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='привью')
    video_url = models.URLField(**NULLABLE, verbose_name='видео')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='пользователь')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Payment(models.Model):
    PAYMENT_TYPE = [
        ('1', 'cach'),
        ('2', 'non-cach'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')
    date = models.DateField(verbose_name='дата платежа')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE, verbose_name='оплаченный урок')
    amount = models.IntegerField(verbose_name='сумма платежа')
    payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPE, verbose_name='тип платежа')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('user', )

    def __str__(self):
        return f'{self.user} - {self.date}: {self.amount}'
