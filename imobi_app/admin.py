from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff',)
    readonly_fields = ('password',)
    search_fields = ('username', 'email')
    list_filter = ('username',)

    def alterar_dados(self, request, user):
        user = User.objects.all()
