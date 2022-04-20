from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "100" style = "border-radius: 50px" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail', 'firstName', 'designation', 'created_date')
    list_display_links = ('id','firstName','thumbnail',)
    search_fields = ('firstName', 'lastName', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)