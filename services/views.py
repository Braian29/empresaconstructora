from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Service, ServiceCategory
from projects.models import Project, ProjectImage # Importamos Project y ProjectImage

def service_list(request):
    selected_category = request.GET.get('category')
    if selected_category:
        services = Service.objects.filter(category__name=selected_category)
    else:
        services = Service.objects.all()
    categories = ServiceCategory.objects.all()
    return render(request, 'services/service_list.html', {'services': services, 'categories': categories, 'selected_category': selected_category})


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # FIX: Usar el related_name correcto desde el modelo Project
        related_projects = self.object.projects_related_to_service.all()

        # Adjuntar la imagen principal a cada proyecto relacionado
        for project in related_projects:
            # Primero intenta obtener la imagen marcada como principal
            main_image = project.images.filter(is_main_image=True).first()
            if not main_image:
                # Si no hay imagen principal, toma la primera disponible
                main_image = project.images.first()
            project.main_image = main_image # Adjuntamos la imagen al objeto project

        context['related_projects'] = related_projects
        return context