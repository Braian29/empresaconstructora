# C:/Users/braia/OneDrive/Escritorio/Aplicaciones_P/Empresa_Constructora/projects/models.py

from django.db import models
from django.utils.text import slugify # ¡IMPORTANTE! Agrega esta línea

class ProjectCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Nombre de la categoría (ej. Residencial, Comercial).")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, help_text="Título del proyecto.")
    # MODIFICACIÓN 1: Agrega blank=True para permitir que el campo esté vacío
    # al momento de la creación/actualización antes de que se autogenere.
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Slug para URLs amigables (se genera automáticamente).")
    short_description = models.CharField(max_length=500, help_text="Breve descripción del proyecto para listados.")
    detailed_description = models.TextField(help_text="Descripción completa y detallada del proyecto.")
    categories = models.ManyToManyField(ProjectCategory, related_name='projects', help_text="Categorías a las que pertenece este proyecto.")
    
    # Campos opcionales para detalles del proyecto
    client = models.CharField(max_length=255, blank=True, null=True, help_text="Nombre del cliente (opcional).")
    location = models.CharField(max_length=255, blank=True, null=True, help_text="Ubicación del proyecto (ej. Buenos Aires, Argentina).")
    duration = models.CharField(max_length=255, blank=True, null=True, help_text="Duración del proyecto (ej. '3 meses', '2022-2023').")
    service_type = models.CharField(max_length=255, blank=True, null=True, help_text="Tipo de servicio (ej. 'Construcción', 'Remodelación', 'Diseño').")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Esto permite vincular proyectos con los servicios que ofreciste para construirlos.
    services = models.ManyToManyField(
        'services.Service', # Referencia al modelo Service en la app 'services'
        related_name='projects_related_to_service', # Nombre inverso para acceder a proyectos desde un servicio
        blank=True, # Un proyecto puede no tener un servicio específico asignado
        help_text="Servicios de la empresa que se utilizaron en este proyecto."
    )

    # Campos para un testimonio específico del cliente sobre este proyecto.
    client_testimonial_quote = models.TextField(
        blank=True,
        null=True,
        help_text="Cita del testimonio de un cliente para este proyecto específico."
    )
    client_testimonial_author = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Nombre del autor del testimonio para este proyecto."
    )

    def __str__(self):
        return self.title

    # MODIFICACIÓN 2: Implementación robusta del método save()
    def save(self, *args, **kwargs):
        # Si el slug no está definido o está vacío
        if not self.slug:
            base_slug = slugify(self.title) # Genera el slug base a partir del título
            unique_slug = base_slug
            num = 1
            # Bucle para asegurar que el slug sea único
            # Si ya existe un proyecto con este slug, añade un número al final
            # .exclude(pk=self.pk) es crucial para que al actualizar un objeto,
            # no se considere a sí mismo como un duplicado.
            while Project.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug # Asigna el slug generado o modificado
        
        super().save(*args, **kwargs) # Llama al método save original de Django


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, help_text="El proyecto al que pertenece esta imagen.")
    image = models.ImageField(upload_to='project_images/', help_text="Archivo de imagen del proyecto.")
    caption = models.CharField(max_length=255, blank=True, null=True, help_text="Leyenda o descripción de la imagen.")
    is_main_image = models.BooleanField(default=False, help_text="Marca si esta es la imagen principal para miniaturas o carruseles.")
    
    def __str__(self):
        return f"Imagen para {self.project.title}" if self.project else f"Imagen sin proyecto asignado"