from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

def get_avatar_filename(instance, filename):
    base_filename , file_extension = os.path.splitext(filename)
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    return os.path.join('user/avastar/', new_filename)

    pass
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=30, unique=True, blank=True)
    avatar = models.ImageField(upload_to=get_avatar_filename, default='user/default/default-avatar-2.png')

    def __str__(self):
        return self.username
    @property
    def is_registered(self):
        return self.groups.filter(name='registered').exists()
    @property
    def is_collaborator(self):
        return self.groups.filter(name='collaborator').exists()
    @property
    def is_admin(self):
        return self.groups.filter(name='admin').exists()
    
    def get_avartar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return None

# Create your models here.
