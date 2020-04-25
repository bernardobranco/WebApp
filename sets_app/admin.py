from django.contrib import admin

# Register your models here.
from .models import Set, Boat, Rider

# admin.site.register(Set)
@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('date_set', 'driver', 'boat', 'duration')
    list_filter = ('date_set', 'boat')

admin.site.register(Boat)
admin.site.register(Rider)