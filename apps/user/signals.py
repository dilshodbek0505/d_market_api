from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .utils import generate_default_avatar

User = get_user_model()


@receiver(post_save, sender=User)
def set_default_avatar(sender, instance, created, **kwargs):
    if created and not instance.avatar:
        instance.avatar.save(f"{instance.name}_avatar.png", generate_default_avatar(instance.name))
