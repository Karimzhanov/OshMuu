from django.contrib import admin

from apps.tests.models import Test
# Register your models here.
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('subject', )
    search_fields = ('subject', )