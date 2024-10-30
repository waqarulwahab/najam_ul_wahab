from django.shortcuts import render, get_object_or_404
from .models import AboutMe
from .models import Client
from .models import Project, ProjectCategory
from .models import ThemeSettings
from .models import AchievementsSection
from .models import Experience
from .models import Service
from .models import BackgroundImage
from .models import Skill
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


import logging
logger = logging.getLogger(__name__)



def index(request):
    theme       = ThemeSettings.objects.first()
    about       = AboutMe.objects.latest('created_at')
    clients     = Client.objects.all()
    categories  = ProjectCategory.objects.all()
    section     = AchievementsSection.objects.first()
    experiences = Experience.objects.all()
    services    = Service.objects.all()
    bg_image    = BackgroundImage.objects.latest('id')
    skills      = Skill.objects.all()

    # Get the total number of projects
    total_projects = Project.objects.count()

    # Determine how many projects to load based on the query parameter
    load_more = int(request.GET.get('load_more', 10))  # Default to 10 if no parameter is provided

    # Get the selected category from the query parameter
    selected_category = request.GET.get('category', '*')

    # Filter projects by the selected category
    projects_with_images_by_category = []
    if selected_category == '*':
        for category in categories:
            projects = Project.objects.filter(category=category)[:load_more]
            for project in projects:
                images = project.images.all()
                projects_with_images_by_category.append({
                    'project': project,
                    'images': images,
                    'category': category,
                })
    else:
        selected_category_obj = ProjectCategory.objects.get(id=selected_category)
        projects = Project.objects.filter(category=selected_category_obj)[:load_more]
        for project in projects:
            images = project.images.all()
            projects_with_images_by_category.append({
                'project': project,
                'images': images,
                'category': selected_category_obj,
            })

    context = {
        'theme': theme,
        'about': about,
        'clients': clients,
        'categories': categories,
        'projects_with_images_by_category': projects_with_images_by_category,
        'section': section,
        'experiences': experiences,
        'services': services,
        'bg_image': bg_image,
        'total_projects': total_projects,
        'loaded_projects': load_more,
        'selected_category': selected_category,  # Pass the selected category to the template
        'skills': skills,
    }
    return render(request, 'index.html', context)







def portfolio_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    images = project.images.all()  # Fetch all images related to this project
    context = {
        'project': project,
        'images': images,  # Pass all the images to the portfolio-details template
    }
    return render(request, 'sections/portfolio-details.html', context)


