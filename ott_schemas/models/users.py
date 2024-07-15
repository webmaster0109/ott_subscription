from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='ott_schemas_user_set',  # Custom related_name to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='ott_schemas_user_set',  # Custom related_name to avoid conflicts
        blank=True
    )

    def __str__(self):
        return self.username
