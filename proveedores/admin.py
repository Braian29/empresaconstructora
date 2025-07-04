# C:/Users/braia/OneDrive/Escritorio/Aplicaciones_P/Empresa_Constructora/proveedores/admin.py

from django.contrib import admin
from .models import Proveedor, ProveedorCategory

@admin.register(ProveedorCategory)
class ProveedorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'website', 'is_featured')
    list_filter = ('is_featured', 'category')
    search_fields = ('name', 'description', 'website')
    list_editable = ('is_featured',)