from django.contrib import admin
from website.models import Tour

class TourAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tour, TourAdmin)
