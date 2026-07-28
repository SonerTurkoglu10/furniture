from django.shortcuts import render
from .models import ShowroomImage

def index(request):
    context = {
        'hero_slides': ShowroomImage.objects.filter(section='hero', is_active=True).order_by('order'),
        'living_room_images': ShowroomImage.objects.filter(section='living_room', is_active=True).order_by('order'),
        'dining_room_images': ShowroomImage.objects.filter(section='dining_room', is_active=True).order_by('order'),
        'bedroom_images': ShowroomImage.objects.filter(section='bedroom', is_active=True).order_by('order'),
        'living_room_title': 'Oturma Odası',
        'dining_room_title': 'Yemek Odası',
        'bedroom_title': 'Yatak Odası',
    }
    return render(request, 'main/index.html', context)
