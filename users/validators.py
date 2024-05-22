import re

from rest_framework.exceptions import ValidationError


class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg1 = re.compile('mail.ru')
        reg2 = re.compile('yandex.ru')
        tmp_val = dict(value).get(self.field)
        if not bool(reg1.findall(tmp_val)) and not bool(reg2.findall(tmp_val)):
            raise ValidationError('разрешены домены: mail.ru, yandex.ru')


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg1 = re.compile(r'[0-9]')
        reg2 = re.compile(r'[a-zA-Z]')
        tmp_val = dict(value).get(self.field)
        if not bool(reg1.findall(tmp_val)) or not bool(reg2.findall(tmp_val)) or len(tmp_val) < 8:
            raise ValidationError('Пароль должен быть не менее 8 символов, должен включать цифры')
