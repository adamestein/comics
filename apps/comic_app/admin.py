from django.contrib import admin

from .models import Comic


class ComicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Comic, ComicAdmin)
