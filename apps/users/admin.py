from django.contrib import admin

from apps.users.models import User, Employee


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name' )
    search_fields = ('username', 'first_name', 'last_name')
    
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone' )
    search_fields = ('first_name', 'last_name', 'phone')
