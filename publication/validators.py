from datetime import datetime
from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        prohibited_list = ['ерунда', 'глупость', 'чепуха']
        for word in prohibited_list:
            if word in val:
                raise ValidationError("В названии Поста есть запрещенные слова")
