import os
from rest_framework.exceptions import ValidationError


def get_patch_upload_cover(instance, file):
    '''
    Построение пути к файлу, format: (media/album/{user_id}/{file_name})
    '''
    return f'album/user_{instance.user.id}/{file}'

def get_patch_upload_avatar(instance, file):
    '''
    Построение пути к файлу, format: (media/avatars/{user_id}/{file_name})
    '''
    return f'avatar/user_{instance.user.id}/{file}'

def get_patch_upload_track(instance, file):
    '''
    Построение пути к файлу, format: (media/track/{user_id}/{file_name})
    '''
    return f'track/user_{instance.user.id}/{file}'

def get_patch_upload_playlist(instance, file):
    '''
    Построение пути к файлу, format: (media/playlist/{user_id}/{file_name})
    '''
    return f'playlist/user_{instance.user.id}/{file}'

def validate_size_image(file_obj):
    '''
    Проверка размера изображения
    '''
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(
            f'Размер файла не должен превышать {megabyte_limit} Мб'
        )
    
def delete_old_file(path_file):
    '''
    Удаление старого файла
    '''
    if os.path.exists(path_file):
        os.remove(path_file)