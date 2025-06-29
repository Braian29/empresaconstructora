from django.shortcuts import render, redirect
from .models import ContactInfo
from .forms import ContactUsForm # Importa la clase del formulario con el nuevo nombre

def contact(request):
    contact_info = ContactInfo.objects.first()
    if request.method == 'POST':
        form = ContactUsForm(request.POST) # Usa el nuevo nombre del formulario
        if form.is_valid():
            form.save()
            return redirect('core:contact_success')
    else:
        form = ContactUsForm() # Usa el nuevo nombre del formulario

    return render(request, 'core/contact.html', {'form': form, 'contact_info': contact_info})


def contact_success(request):
    return render(request, 'core/contact_success.html')