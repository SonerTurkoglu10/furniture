from django.contrib import admin
from django.urls import path
from contact import views  # veya iletişim uygulamanın adı neyse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
]
