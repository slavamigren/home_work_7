from rest_framework.serializers import ValidationError


class URLValidator:
    """Валидатор проверяет, что ссылка на видео с youtube"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field, None) and 'youtube.com/' not in value.get(self.field):
            raise ValidationError('Допустимы только видео с youtube')
