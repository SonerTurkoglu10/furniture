from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='home'),
    path('randevu/', contact_views.home_view, name='appointment'),
    path('randevu/submit/', contact_views.appointment_submit, name='appointment_submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
