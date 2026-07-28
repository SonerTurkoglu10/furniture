from django.contrib import admin
from django.utils.html import format_html
from .models import ShowroomImage

@admin.register(ShowroomImage)
class ShowroomImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'section', 'order', 'is_active', 'created_at')
    list_filter = ('section', 'is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_large')
    list_editable = ('order', 'is_active',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;"/>',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Önizleme'

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 300px;"/>',
                obj.image.url
            )
        return "No Image"
    image_preview_large.short_description = 'Görsel Önizleme'

    fieldsets = (
        ('Görsel', {
            'fields': ('image', 'image_preview_large')
        }),
        ('Ayarlar', {
            'fields': ('section', 'order', 'is_active')
        }),
        ('Zaman Bilgileri', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )