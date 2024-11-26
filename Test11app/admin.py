from django.contrib import admin
from .models import CheckTab


@admin.action(description='Reset selected events to original conditions')
def reset_to_original(modeladmin, request, queryset):
    for event in queryset:
        event.revert_condition()
        event.save()


@admin.register(CheckTab)
class CheckTabAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'date', 'slot_of_day', 'event', 'temperature',
                    'condition', 'special', 'is_modified', 'original_condition')
    list_filter = ('city', 'date', 'slot_of_day', 'is_modified')
    search_fields = ('city', 'event', 'condition', 'special')
    actions = [reset_to_original]
    readonly_fields = ('is_modified',)  # Prevent direct editing of calculated fields in admin

    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'city', 'date', 'slot_of_day', 'event', 'temperature')
        }),
        ('Conditions', {
            'fields': ('condition', 'special', 'original_condition', 'is_modified')
        }),
    )
