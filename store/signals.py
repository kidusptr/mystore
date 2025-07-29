from .models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        Customer.objects.create(user=kwargs["instance"])
