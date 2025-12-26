from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models.user import User


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
