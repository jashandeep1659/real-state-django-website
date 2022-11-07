from django.contrib import admin
from .models import *


class AutoFillSlug(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }


class BuildingImages(admin.TabularInline):
    model = Building_images
    fields = ("image", "index")


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [
        BuildingImages,
    ]


admin.site.register(City, AutoFillSlug)
admin.site.register(Category, AutoFillSlug)
admin.site.register(TypeOf, AutoFillSlug)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Building_images)
admin.site.register(HandPick)
admin.site.register(Chat)
admin.site.register(Message)
