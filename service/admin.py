from django.contrib import admin

from service.models import ServiceSeeker


class ServiceSeekerAdmin(admin.ModelAdmin):
    list_display = ('seeker_ip', 'loc_latitude', 'loc_longitude',)


admin.site.register(ServiceSeeker, ServiceSeekerAdmin)
