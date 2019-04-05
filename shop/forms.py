from django.contrib.auth.forms import UserCreationForm

from .models import Client



class ClientForm(UserCreationForm):
    class Meta:
        model = Client
        exclude = (
            'last_login',
            'is_staff',
            'is_superuser',
            'date_joined',
            'groups',
            'user_permissions',
            'password',
            'is_active',
        )
        fields = '__all__'
