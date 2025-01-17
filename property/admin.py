from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerFlatsInstanceInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner', 'flat']


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('address',
                     'town',
                     'pk'
                     )
    readonly_fields = ['created_at']
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town'
                    )
    list_editable = ['new_building']
    list_filter = ('new_building',
                   'has_balcony',
                   'rooms_number'
                   )
    raw_id_fields = ['liked_by']
    inlines = [OwnerFlatsInstanceInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['from_user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    inlines = [OwnerFlatsInstanceInline]
