from django.contrib import admin
from .models import TeamMember, Testimonial, Value, AboutUs

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'image')
    list_filter = ('title',) 
    search_fields = ('name', 'title', 'bio')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'short_text', 'image')
    list_filter = ('client_name',)
    search_fields = ('client_name', 'content')

    def short_text(self, obj):
        return obj.content[:50] + "..."
    short_text.short_description = 'Testimonial Excerpt'

@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    list_filter = ('name',)
    search_fields = ('name', 'description')

    def short_description(self, obj):
        return obj.description[:50] + "..."
    short_description.short_description = 'Description Excerpt'

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    filter_horizontal = ('values', 'team_members', 'testimonials')