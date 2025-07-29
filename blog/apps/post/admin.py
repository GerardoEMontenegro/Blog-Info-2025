from django.contrib import admin
from apps.post.models import *
from apps.user.models import User


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'created_at', 'updated_at', 'allow_comments')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author', 'created_at', 'allow_comments')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('title','author__user_name', 'id', '')
    list_filter = ('post', 'author', 'created_at')

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'email', 'is_registered', 'is_collaborator', 'is_admin')
#     search_fields = ('user_name', 'email')
#     list_filter = ('is_registered', 'is_collaborator', 'is_admin')








admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(User, UserAdmin)