# C:/Users/braia/OneDrive/Escritorio/Aplicaciones_P/Empresa_Constructora/proveedores/models.py

from django.db import models

class ProveedorCategory(models.Model):
    """
    Categoría para agrupar proveedores (ej. Materiales, Maquinaria, Servicios).
    """
    name = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría del proveedor.")
    
    class Meta:
        verbose_name = "Categoría de Proveedor"
        verbose_name_plural = "Categorías de Proveedores"

    def __str__(self):
        return self.name

class Proveedor(models.Model):
    """
    Representa a un proveedor o socio comercial.
    """
    name = models.CharField(max_length=255, help_text="Nombre del proveedor.")
    logo = models.ImageField(upload_to='proveedores_logos/', help_text="Logo del proveedor. Idealmente cuadrado o con fondo transparente.")
    website = models.URLField(max_length=255, blank=True, null=True, help_text="Sitio web del proveedor (opcional).")
    description = models.TextField(blank=True, null=True, help_text="Breve descripción de lo que provee o su relación con la empresa (opcional).")
    category = models.ForeignKey(
        ProveedorCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='proveedores',
        help_text="Categoría a la que pertenece el proveedor (opcional)."
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Marcar si este proveedor debe aparecer en la página de inicio."
    )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['name']

    def __str__(self):
        return self.name