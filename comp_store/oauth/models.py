from django.db import models
from django.core.validators import FileExtensionValidator

from base.services import get_path_upload_avatar, validate_size_image

class AuthUser(models.Model):
    """Кастомная модель пользователя
    """
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.CharField(max_length=50, )
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name='Страна')
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name='Город')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=get_path_upload_avatar, 
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    def __str__(self) -> str:
        return self.email

    @property
    def is_authenticated(self):
        """Аутентифицирован ли пользователь
        """
        return True
