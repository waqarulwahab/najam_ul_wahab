from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import AboutMe
from .models import Client
from .models import Project, ProjectCategory
from .models import ThemeSettings
from .models import AchievementsSection
from .models import Experience
from .models import Service

# Create your views here.
def index(request):
    theme = ThemeSettings.objects.first()  # Fetch the first instance of theme settings
    about = AboutMe.objects.latest('created_at')  # Get the latest entry based on creation time
    clients = Client.objects.all()

    categories = ProjectCategory.objects.all()
    projects = Project.objects.all()

    section = AchievementsSection.objects.first()  # Get the first record

    # Add images to each project
    projects_with_images = []
    for project in projects:
        images = project.images.all()  # Get all images related to the project
        projects_with_images.append({
            'project': project,
            'images': images,
        })

    # Pagination - Display 5 projects per page
    paginator = Paginator(projects_with_images, 12)  # Show 5 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    experiences = Experience.objects.all()
    services    = Service.objects.all()

    context = {
        'theme': theme,
        'about': about,
        'clients': clients,
        'categories': categories,
        'projects_with_images': page_obj,  # Passing paginated projects with their images
        'section': section,
        'page_obj': page_obj,  # For pagination controls
        'experiences': experiences,
        'services': services,
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


