from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "category", "author")


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.User)
