from rest_framework.exceptions import ValidationError

def validate_size_image(value):
    '''
    Проверка размера изображения
    '''
    megabite_limit = 2
    if value.size > megabite_limit * 1024 * 1024:
        raise ValidationError(
            'Размер изображения не должен превышать 2 мегабайта'
        )