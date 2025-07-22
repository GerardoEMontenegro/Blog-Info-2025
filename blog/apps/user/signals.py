from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            # Add your logic here, for example:
            registered_group, created = Group.objects.get_or_create(
                ame='registered'
                )
            registered_group.permissions.add(
            #     *Permission.objects.filter(codename__startswith='view_')
                )


            collaborator_group, created = Group.objects.get_or_create(
                name='collaborator'
                )
            
            registered_group.permissions.add(
            #     *Permission.objects.filter(codename__startswith='view_')
                )
            
            admin_group, created = Group.objects.get_or_create(
                name='admin'
                )
            registered_group.permissions.add(
            #     *Permission.objects.filter(codename__startswith='view_')
                )
            
            pass
        except ContentType.DoesNotExist: 
            print("El tipo de contenido no existe.")
        except Permission.DoesNotExist:
            print("El permiso no existe.")
            pass