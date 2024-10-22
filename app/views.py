from django.shortcuts import render, get_object_or_404
from .models import AboutMe
from .models import Client
from .models import Project, ProjectCategory
from .models import ThemeSettings
from .models import AchievementsSection
from .models import Experience
from .models import Service
from .models import BackgroundImage
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


import logging
logger = logging.getLogger(__name__)



def index(request):
    theme = ThemeSettings.objects.first()
    about = AboutMe.objects.latest('created_at')
    clients = Client.objects.all()
    categories = ProjectCategory.objects.all()
    section = AchievementsSection.objects.first()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    bg_image = BackgroundImage.objects.latest('id')
    
    # Get the total number of projects to send to the template
    total_projects = Project.objects.count()

    projects = Project.objects.all()
    projects_with_images = []
    for project in projects:
        images = project.images.all()
        projects_with_images.append({
            'project': project,
            'images': images,
        })

    context = {
        'theme': theme,
        'about': about,
        'clients': clients,
        'categories': categories,
        'projects_with_images': projects_with_images,
        'section': section,
        'experiences': experiences,
        'services': services,
        'bg_image': bg_image,
        'total_projects': total_projects,
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


