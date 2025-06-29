# C:/Users/braia/OneDrive/Escritorio/Aplicaciones_P/Empresa_Constructora/services/models.py

from django.db import models
from django.utils.text import slugify

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Nombre de la categoría de servicio (ej. Construcción Residencial).")
    description = models.TextField(blank=True, help_text="Descripción de la categoría de servicio.")
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True, help_text="Icono representativo de la categoría (opcional).")

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services', help_text="Categoría a la que pertenece este servicio.")
    title = models.CharField(max_length=255, help_text="Título del servicio.")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Slug para URLs amigables (se genera automáticamente).")
    description = models.TextField(help_text="Descripción detallada del servicio.")
    short_description = models.CharField(max_length=255, help_text="Breve descripción del servicio para listados o tarjetas.") # Este campo ya estaba y se mantiene
    image = models.ImageField(upload_to='service_images/', blank=True, null=True, help_text="Imagen principal del servicio.")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# ELIMINADO: class Project(models.Model): de este archivo
# ELIMINADO: class ProjectImage(models.Model): de este archivo
# ELIMINADO: class Testimonial(models.Model): de este archivo