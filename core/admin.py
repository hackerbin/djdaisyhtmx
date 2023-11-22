from django.contrib import admin
from django.contrib.admin import site

from core.models import Todo, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
