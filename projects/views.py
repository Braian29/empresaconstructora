from django.shortcuts import render
from .models import Project, ProjectCategory
from services.models import ServiceCategory
from about.models import AboutUs, Value
from projects.models import ProjectImage 
from proveedores.models import Proveedor 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    featured_projects = Project.objects.all().order_by('-created_at')[:3]
    featured_services = ServiceCategory.objects.all()[:3]
    about_us_snippet = AboutUs.objects.first()
    values = Value.objects.all()
    # 2. OBTÉN LOS PROVEEDORES DESTACADOS
    proveedores_destacados = Proveedor.objects.filter(is_featured=True)

    # Fetch images and videos for the carousel.  This example assumes you have a main image marked for projects.
    hero_carousel_items = []
    featured_project_images = ProjectImage.objects.filter(is_main_image=True)  # Assuming 'is_main_image' is defined
    for image in featured_project_images:
        hero_carousel_items.append({'image_url': image.image.url, 'caption': image.caption, 'video_url': None}) # Add video_url for consistency


    context = {
        'featured_projects': featured_projects,
        'featured_services': featured_services,
        'about_us_snippet': about_us_snippet,
        'values': values,
        'carousel_items': hero_carousel_items, # Correct the key name
        'proveedores_destacados': proveedores_destacados, # <-- 3. AÑADE AL CONTEXTO
    }

    return render(request, 'core/home.html', context)


def project_list(request):
    selected_categories = request.GET.getlist('category', [])
    if selected_categories:
        projects = Project.objects.filter(categories__name__in=selected_categories)
    else:
        projects = Project.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(projects, 6)  # 6 projects per page

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)


    categories = ProjectCategory.objects.all() # Pass all categories for filter display
    context = {
        'project_list': projects,
        'categories': categories,
        'selected_categories': selected_categories, # Pass selected categories to maintain filter state
        'is_paginated': projects.has_other_pages(),
        'page_obj': projects,

    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})