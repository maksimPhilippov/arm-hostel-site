from django.contrib import admin
from website.models import Tour, Room, RoomPhoto

class TourAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class RoomPhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tour, TourAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomPhoto, RoomPhotoAdmin)
