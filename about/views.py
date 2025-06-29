from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs # Solo necesitamos importar AboutUs aquí

class AboutUsView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtenemos la primera (y única esperada) instancia de AboutUs
        about_us_obj = AboutUs.objects.first()

        if about_us_obj:
            context['about_us'] = about_us_obj
            context['main_content'] = about_us_obj.main_content
            context['mission'] = about_us_obj.mission
            context['vision'] = about_us_obj.vision
            # Accedemos a los relacionados a través de las relaciones ManyToMany
            context['values'] = about_us_obj.values.all()
            context['team_members'] = about_us_obj.team_members.all()
            context['testimonials'] = about_us_obj.testimonials.all()
        else:
            # Proporcionar valores por defecto o mensajes si no hay objeto AboutUs
            context['about_us'] = None
            context['main_content'] = "Contenido principal de Quiénes Somos aún no configurado en el panel de administración."
            context['mission'] = "Misión de la empresa aún no configurada."
            context['vision'] = "Visión de la empresa aún no configurada."
            context['values'] = []
            context['team_members'] = []
            context['testimonials'] = []

        # La variable 'about_images' no tiene un campo directo en el modelo AboutUs,
        # si se necesitan imágenes adicionales para la sección "Quiénes Somos"
        # que no sean parte del main_content, se debería añadir un nuevo modelo
        # o campo al modelo AboutUs. Por ahora, lo dejamos vacío para evitar errores.
        context['about_images'] = []

        return context