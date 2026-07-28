from django import forms
from .models import Appointment
import re

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'message']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Remove all non-digit characters
        phone = re.sub(r'\D', '', phone)
        
        # Check if it's a valid Turkish phone number
        if not re.match(r'^5\d{9}$', phone) and not re.match(r'^0?5\d{9}$', phone):
            raise forms.ValidationError('Lütfen geçerli bir telefon numarası giriniz (5XX XXX XX XX formatında)')
        
        # Standardize format to 5XX XXX XX XX
        if phone.startswith('0'):
            phone = phone[1:]
        return phone

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.split()) < 2:
            raise forms.ValidationError('Lütfen ad ve soyadınızı giriniz')
        return name