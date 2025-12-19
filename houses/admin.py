from django.contrib import admin
from .models import House, HouseImage

class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'bedrooms', 'bathrooms')
    inlines = [HouseImageInline]

@admin.register(HouseImage)
class HouseImageAdmin(admin.ModelAdmin):
    list_display = ('house', 'category', 'image')
