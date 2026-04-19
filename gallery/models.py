from django.db import models

from utils.validators import (
    validate_file_extension,
    validate_file_size,
    validate_image_extension,
    validate_image_size,
)


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='photos/images/',
        validators=[validate_image_size, validate_image_extension],
    )
    file = models.FileField(
        upload_to='photos/files/',
        validators=[validate_file_size, validate_file_extension],
        blank=True,
        null=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
