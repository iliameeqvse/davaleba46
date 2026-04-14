from django.contrib.auth.models import User
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    followers_count = models.PositiveIntegerField(default=0)
    posts_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} profile'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_relations')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_relations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'], name='unique_follow_relation'),
            models.CheckConstraint(check=~models.Q(user=models.F('following')), name='prevent_self_follow'),
        ]

    def __str__(self):
        return f'{self.user.username} follows {self.following.username}'
