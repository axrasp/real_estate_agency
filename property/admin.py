from django.contrib import admin

from .models import Flat, Complaint, Owner


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('address', 'town', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price',
                    'new_building',
                    'construction_year',
                    'owner_pure_phone',
                    'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'has_balcony', 'rooms_number')
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['from_user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

