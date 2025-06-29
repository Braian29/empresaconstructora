# core/context_processors.py
from .models import ContactInfo

def contact_info_processor(request):
    """
    Agrega la primera instancia de ContactInfo al contexto de todas las solicitudes.
    """
    try:
        contact_info = ContactInfo.objects.first()
    except ContactInfo.DoesNotExist:
        contact_info = None # En caso de que no haya ninguna ContactInfo creada
    return {'contact_info': contact_info}