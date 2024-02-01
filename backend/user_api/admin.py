from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminForm

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
    )
    list_filter = ("role", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("id",)
    list_display_links = ("email",)

    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "mobile_number",
                    "role",
                    "password",
                    "uid",
                )
            },
        ),
        (
            "Important dates",
            {"fields": ("date_joined", "modified_date", "last_login")},
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "is_deleted")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "role",
                ),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        # Add the fields you want to make read-only here
        return readonly_fields + (
            "uid",
            "password",
            "modified_date",
            "last_login",
            "date_joined",
        )


admin.site.register(User, CustomUserAdmin)
