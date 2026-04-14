import os

from django.core.exceptions import ValidationError


IMAGE_ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
FILE_ALLOWED_EXTENSIONS = {'pdf', 'txt'}
IMAGE_MAX_SIZE = 2 * 1024 * 1024
FILE_MAX_SIZE = 5 * 1024 * 1024


def _validate_extension(file_obj, allowed_extensions):
    ext = os.path.splitext(file_obj.name)[1].lower().replace('.', '')
    if ext not in allowed_extensions:
        raise ValidationError(f'Unsupported extension: {ext}. Allowed: {", ".join(sorted(allowed_extensions))}')


def validate_image_size(image):
    if image.size > IMAGE_MAX_SIZE:
        raise ValidationError('Image size must be 2MB or less.')


def validate_image_extension(image):
    _validate_extension(image, IMAGE_ALLOWED_EXTENSIONS)


def validate_file_size(file_obj):
    if file_obj.size > FILE_MAX_SIZE:
        raise ValidationError('File size must be 5MB or less.')


def validate_file_extension(file_obj):
    _validate_extension(file_obj, FILE_ALLOWED_EXTENSIONS)
