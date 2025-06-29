from django import forms
from .models import ContactForm as ContactFormModel # Importa el modelo con un alias

class ContactUsForm(forms.ModelForm): # Cambia el nombre de la clase
    class Meta:
        model = ContactFormModel  # Usa el alias del modelo
        fields = '__all__'