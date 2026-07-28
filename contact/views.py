from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment

def home_view(request):
    return render(request, 'main/index.html')

def appointment_submit(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Randevu talebiniz başarıyla alınmıştır. En kısa sürede sizinle iletişime geçeceğiz.')
            return redirect('home')
        else:
            messages.error(request, 'Lütfen formu eksiksiz ve doğru doldurunuz.')
            return redirect('home')
    return redirect('home')
