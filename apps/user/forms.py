from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see "
            "the user’s password."
        ),
    )

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            if self.instance and not self.instance.has_usable_password():
                password.help_text = _(
                    "Enable password-based authentication for this user by setting a "
                    "password."
                )
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )


class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("phone_number", "name")  # Kerakli fieldlar ro'yxati

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Telefon raqami"
        self.fields['name'].label = "Ism"
        self.fields['password1'].label = "Parol"
        self.fields['password2'].label = "Parolni tasdiqlang"

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Telefon raqami formatini tekshirish (ixtiyoriy)
        if not phone_number:
            raise forms.ValidationError("Telefon raqami kiritilishi kerak.")
        return phone_number
