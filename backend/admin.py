from django.contrib import admin
from .models import Donation, Destination, Department, Stage, Company, Store, DiversionType

class DonationAdmin(admin.ModelAdmin):
    list_display = ('creation_time', 'store', 'weight_kg', 'department', 'destination', 'notes')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'stage', 'diversion_type')


admin.site.register(Donation, DonationAdmin)
admin.site.register(Destination)
admin.site.register(Department)
admin.site.register(Stage)
admin.site.register(Company)
admin.site.register(Store, StoreAdmin)
admin.site.register(DiversionType)
