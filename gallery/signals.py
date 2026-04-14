from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Follow, Post, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Post)
def handle_post_created(sender, instance, created, **kwargs):
    if not created:
        return

    profile, _ = Profile.objects.get_or_create(user=instance.author)
    profile.posts_count += 1
    profile.save(update_fields=['posts_count'])
    print(f'New post created by {instance.author.username}')


@receiver(post_delete, sender=Post)
def handle_post_deleted(sender, instance, **kwargs):
    profile, _ = Profile.objects.get_or_create(user=instance.author)
    profile.posts_count = max(profile.posts_count - 1, 0)
    profile.save(update_fields=['posts_count'])
    print(f'Post deleted: {instance.title}')


@receiver(post_save, sender=Follow)
def handle_follow_created(sender, instance, created, **kwargs):
    if not created:
        return

    profile, _ = Profile.objects.get_or_create(user=instance.following)
    profile.followers_count += 1
    profile.save(update_fields=['followers_count'])


@receiver(post_delete, sender=Follow)
def handle_follow_deleted(sender, instance, **kwargs):
    profile, _ = Profile.objects.get_or_create(user=instance.following)
    profile.followers_count = max(profile.followers_count - 1, 0)
    profile.save(update_fields=['followers_count'])
