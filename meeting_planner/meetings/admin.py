from django.contrib import admin

from .models import Meeting, Room, Comment


admin.site.register(Meeting)
admin.site.register(Room)
admin.site.register(Comment)