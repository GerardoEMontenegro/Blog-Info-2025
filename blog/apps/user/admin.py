from django.contrib import admin
from apps.user.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('alias', 'avatar')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'alias', 'avatar', 'password1', 'password2')
        }),
    )

    def is_registered(self, obj):
        return obj.groups.filter(name='Registered').exists()
    is_registered.boolean = True
    is_registered.short_description = 'Usuario registrado'

    def is_admin(self, obj):
        return obj.groups.filter(name='Admin').exists()
    is_admin.boolean = True
    is_admin.short_description = 'Usuario administrador'

    def is_collaborator(self, obj):
        return obj.groups.filter(name='Collaborator').exists()
    is_collaborator.boolean = True
    is_collaborator.short_description = 'Usuario colaborador'
    
    def add_to_registered(self, request, queryset):
        registered_group = Group.objects.get(name='Registered')
        for user in queryset:
            user.groups.add(Group.objects.get(name='Registered'))
        self.message_user(request, "Usuarios registrados correctamente")
    add_to_registered.short_description = 'Agregar usuarios a grupo Registrados'

    def add_to_admin(self, request, queryset):
        admin_group = Group.objects.get(name='Admin')
        for user in queryset:
            user.groups.add(admin_group)
        self.message_user(request, "Usuarios administradores correctamente")
    add_to_admin.short_description = 'Agregar usuarios a grupo Administradores'

    def add_to_collaborator(self, request, queryset):
        collaborator_group = Group.objects.get(name='Collaborator')
        for user in queryset:
            user.groups.add(collaborator_group)
        self.message_user(request, "Usuarios colaboradores correctamente")
    add_to_collaborator.short_description = 'Agregar usuarios a grupo Colaboradores'

    def remove_to_registered(self, request, queryset):
        registered_group = Group.objects.get(name='Registered')
        for user in queryset:
            user.groups.remove(Group.objects.get(name='Registered'))
        self.message_user(request, "Usuarios registrados correctamente")
    remove_to_registered.short_description = 'Eliminar usuarios a grupo Registrados'

    def remove_to_admin(self, request, queryset):
        admin_group = Group.objects.get(name='Admin')
        for user in queryset:
            user.groups.remove(admin_group)
        self.message_user(request, "Usuarios administradores correctamente")
    remove_to_admin.short_description = 'Eliminar usuarios a grupo Administradores'

    def remove_to_collaborator(self, request, queryset):
        collaborator_group = Group.objects.get(name='Collaborator')
        for user in queryset:
            user.groups.remove(collaborator_group)
        self.message_user(request, "Usuarios colaboradores correctamente")
    remove_to_collaborator.short_description = 'Eliminar usuarios a grupo Colaboradores'

    list_display = ('username', 'email', 'is_staff', 'is_active',
                    'is_superuser', 'is_registered', 'is_admin', 'is_collaborator')

    actions = [
        'add_to_registered',
        'add_to_admin',
        'add_to_collaborator',
        ]





admin.site.register(User, UserAdmin)