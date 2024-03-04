from django.contrib import admin
from . import models

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.AvailableTime)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)
