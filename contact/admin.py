from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'message')
    list_display_links = ('name', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)  # En yeni randevular üstte
    list_per_page = 20  # Sayfa başına gösterilecek randevu sayısı
