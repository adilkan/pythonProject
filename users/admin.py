from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_staff']
    search_fields = ['username']


admin.site.register(User, UserAdmin)