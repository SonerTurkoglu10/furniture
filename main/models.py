from django.db import models

class ShowroomImage(models.Model):
    SECTION_CHOICES = [
        ('hero', 'Ana Sayfa Slider'),
        ('living_room', 'Oturma Odası'),
        ('dining_room', 'Yemek Odası'),
        ('bedroom', 'Yatak Odası'),
    ]

    image = models.ImageField(upload_to='showroom/', verbose_name="Görsel")
    section = models.CharField(
        max_length=20, 
        choices=SECTION_CHOICES,
        verbose_name="Bölüm"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Showroom Görseli"
        verbose_name_plural = "Showroom Görselleri"
        ordering = ['section', 'order', '-created_at']

    def __str__(self):
        # The `title` field was removed; use a stable identifier instead
        try:
            identifier = self.image.name.split('/')[-1] if self.image and getattr(self.image, 'name', None) else f"id:{self.pk}"
        except Exception:
            identifier = f"id:{self.pk}"
        return f"{self.get_section_display()} - {identifier}"