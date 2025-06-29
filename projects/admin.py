from django.contrib import admin
from .models import Project, ProjectCategory, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_categories', 'created_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'detailed_description')
    inlines = [ProjectImageInline]
    prepopulated_fields = {'slug': ('title',)}

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = "Categories"

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)