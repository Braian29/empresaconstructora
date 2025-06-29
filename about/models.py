# C:/Users/braia/OneDrive/Escritorio/Aplicaciones_P/Empresa_Constructora/about/models.py

from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, help_text="Cargo o posición del miembro del equipo (ej. Arquitecto, Fundador).")
    bio = models.TextField(blank=True, help_text="Breve biografía o descripción del miembro.")
    image = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Foto del miembro del equipo.")

    def __str__(self):
        return self.name

class Value(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Nombre del valor (ej. Innovación, Compromiso).")
    description = models.TextField(help_text="Descripción detallada del valor.")
    icon = models.ImageField(upload_to='values/', blank=True, null=True, help_text="Icono que representa el valor.")
    # Nota: si usas íconos de FontAwesome, podrías tener un campo CharField para el nombre de la clase (ej. 'fas fa-lightbulb').

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    """
    Este modelo representa testimonios generales que pueden aparecer en varias secciones
    del sitio (ej. página de inicio, página "Quiénes Somos").
    """
    client_name = models.CharField(max_length=255, help_text="Nombre del cliente que da el testimonio.")
    content = models.TextField(help_text="Contenido del testimonio.")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Foto del cliente (opcional).")
    
    # Podrías añadir un campo para el proyecto si el testimonio es de un proyecto en particular
    # project_related = models.ForeignKey('projects.Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='general_testimonials_from_project')

    def __str__(self):
        return f"Testimonio de {self.client_name}"

class AboutUs(models.Model):
    title = models.CharField(
        max_length=255, 
        default="Quiénes Somos", # Cambiado a español
        help_text="Título de la sección 'Quiénes Somos' (para futuras traducciones o variaciones)."
    )
    main_content = models.TextField(help_text="Contenido principal de la sección 'Quiénes Somos' (ej. historia de la empresa).")
    mission = models.TextField(blank=True, help_text="Declaración de la misión de la empresa.")
    vision = models.TextField(blank=True, help_text="Declaración de la visión de la empresa.")
    
    # Relaciones Many-to-Many con otros modelos para poblar dinámicamente la sección
    values = models.ManyToManyField(
        Value, 
        related_name='about_sections', 
        blank=True,
        help_text="Valores asociados a la sección 'Quiénes Somos'."
    )
    team_members = models.ManyToManyField(
        TeamMember, 
        related_name='about_sections', 
        blank=True,
        help_text="Miembros del equipo destacados en la sección 'Quiénes Somos'."
    )
    testimonials = models.ManyToManyField(
        Testimonial, 
        related_name='about_sections', 
        blank=True,
        help_text="Testimonios destacados en la sección 'Quiénes Somos'."
    )

    class Meta:
        verbose_name_plural = "Quiénes Somos" # Forma plural correcta en español

    def __str__(self):
        return self.title