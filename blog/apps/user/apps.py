from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        from django.contrib.auth.models import Group
        import apps.user.signals

        # Asegurar existencia de grupos
        for group_name in ['Registered', 'Collaborators', 'Admins']:
            Group.objects.get_or_create(name=group_name)
