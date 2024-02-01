from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class CustomUser(UserAdmin):
    model = User
    list_display = (
        "role",
        "email",
        "date_joined",
        "is_active",
        "created_by",
    )
    list_filter = ("role", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-date_joined",)
    form = CustomUserAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        # Add the fields you want to make read-only here
        return readonly_fields + (
            "uid",
            "password",
            "modified_date",
            "last_login",
            "created_by",
            "date_joined",
        )

    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "password",
                    "uid",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "is_deleted")},
        ),
        (
            "Important dates",
            {"fields": ("date_joined", "modified_date", "last_login")},
        ),
        ("Audit Info", {"fields": ["created_by", "modified_by"]}),
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


admin.site.register(User, CustomUser)
