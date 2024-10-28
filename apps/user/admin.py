from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ModelAdmin
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserChangeForm, AdminUserCreationForm


class UserAdmin(ModelAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal info"), {"fields": ("name", "username", "telegram_id", "avatar")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "name", "password1", "password2"),
            },
        ),
    )
    add_form = AdminUserCreationForm
    form = UserChangeForm
    list_display = ("phone_number", "name", "username", "telegram_id", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("phone_number", "username", "telegram_id")
    ordering = ("created_at",)
    
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(User, UserAdmin)