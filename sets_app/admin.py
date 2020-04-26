from django.contrib import admin

# Register your models here.
from .models import Set, Boat, Rider

# admin.site.register(Set)
@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('date_set', 'driver', 'boat', 'duration')
    list_filter = ('date_set', 'boat')


#admin.site.register(Boat)
@admin.register(Boat)
class SetBoat(admin.ModelAdmin):
    list_display = ('brand', 'model', 'date_added')

#admin.site.register(Rider)
@admin.register(Rider)
class SetRider(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nationality', 'date_of_birth')