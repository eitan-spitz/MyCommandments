from django.contrib import admin
from account_app.models import Commandments

# Register your models here.
class CommandmentAdmin(admin.ModelAdmin):
    list_display = ('my_order', 'mitzvah', 'book')
    list_per_page = 100
    ordering = ['my_order']


admin.site.register(Commandments, CommandmentAdmin)