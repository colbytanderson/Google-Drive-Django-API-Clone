from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model as user_model
User = user_model()
from django.contrib import admin

admin.site.register(User, UserAdmin)