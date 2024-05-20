from datetime import datetime
from rest_framework.serializers import ValidationError


class AutorBirthDayValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        birthdate_str = dict(value).get(self.field)
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.now().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age is not None and age < 18:
            raise ValidationError("Автор поста не достиг возраста 18 лет")


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        prohibited_list = ['ерунда', 'глупость', 'чепуха']
        for word in prohibited_list:
            if word in val:
                raise ValidationError("В названии Поста есть запрещенные слова")
