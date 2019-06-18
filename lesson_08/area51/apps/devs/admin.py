from django.contrib import admin
from apps.devs.models import Company, Software, Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email')
    search_fields = ('name', 'email')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')
    search_fields = ('name', 'website')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Software)
admin.site.register(Developer, DeveloperAdmin)
