from django.db import models
from colorfield.fields import ColorField  # Import the color picker field
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.



class AboutMe(models.Model):
    name          = models.CharField(max_length=255, default='NAJM UL WAHAB',    null=True, blank=True)
    title         = models.CharField(max_length=255, default='Architecture', null=True, blank=True)
    birthday      = models.DateField()
    website       = models.URLField(max_length=255, null=True, blank=True)
    phone         = models.CharField(max_length=20)
    city          = models.CharField(max_length=100)
    age           = models.IntegerField()
    degree        = models.CharField(max_length=100)
    email         = models.EmailField()
    freelance     = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Not Available', 'Not Available')])
    profile_image = models.ImageField(upload_to='about/')
    bio           = models.TextField()
    created_at    = models.DateTimeField(auto_now_add=True)  # New field for creation timestamp

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clients/logos/')
    
    def __str__(self):
        return self.name
    
class ProjectCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

def project_image_path(instance, filename):
    # If the project has a title, use it in the file path, otherwise only use the category name
    if instance.project.title:
        # Slugify the title to make it URL-safe (optional, but recommended)
        title_folder = instance.project.title.replace(' ', '_')  # Replace spaces with underscores
        return f'portfolio/{instance.project.category.name}/{title_folder}/{filename}'
    else:
        # Fallback to using just the category name if title is None
        return f'portfolio/{instance.project.category.name}/{filename}'

class Project(models.Model):
    YES_NO_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]
    title             = models.CharField(max_length=255, null=True, blank=True)
    description       = models.TextField(null=True, blank=True)
    category          = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    project_url       = models.URLField(null=True, blank=True)
    client_name       = models.CharField(max_length=255, null=True, blank=True)  # Client name
    project_date      = models.DateField(null=True, blank=True)  # Project date

    detail_title      = models.CharField(max_length=255, null=True, blank=True)
    detail_description = models.TextField(null=True, blank=True)
    display_details   = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='NO')

    def __str__(self):
        return self.title if self.title else "Unnamed Project"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image   = models.ImageField(upload_to=project_image_path)  # Image upload path handled here

    def __str__(self):
        return f"Image for {self.project.title}"
    
class AchievementsSection(models.Model):
    title            = models.CharField(max_length=255, default="What we have achieved so far")
    description      = models.TextField(default="Crafting innovative spaces with precision and creativity, building structures that stand the test of time.")
    clients          = models.IntegerField(default=0)
    projects         = models.IntegerField(default=0)
    hours_of_support = models.IntegerField(default=0)
    experience       = models.IntegerField(default=0)  # For Hard Workers / Experience

    def __str__(self):
        return self.title

class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    position     = models.CharField(max_length=255)
    start_year   = models.IntegerField()
    end_year     = models.IntegerField(null=True, blank=True)  # For ongoing roles, leave blank
    description  = models.TextField()
    image        = models.ImageField(upload_to='experience_images/')  # Assumes you have media files handling set up

    def __str__(self):
        return f"{self.company_name} ({self.start_year} - {self.end_year or 'Present'})"
    
class Service(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    icon_image  = models.ImageField(upload_to='service_icons/')  # Upload path for the service icons

    def __str__(self):
        return self.title



class ThemeSettings(models.Model):
    background_color   = ColorField(default="#ffffff")
    default_color      = ColorField(default="#212529")
    heading_color      = ColorField(default="#37373f")
    accent_color       = ColorField(default="#ce1212")
    surface_color      = ColorField(default="#ffffff")
    contrast_color     = ColorField(default="#ffffff")
    
    nav_color                     = ColorField(default="#7f7f90")
    nav_hover_color               = ColorField(default="#ce1212")
    nav_mobile_background_color   = ColorField(default="#ffffff")
    nav_dropdown_background_color = ColorField(default="#ffffff")
    nav_dropdown_color            = ColorField(default="#7f7f90")
    nav_dropdown_hover_color      = ColorField(default="#ce1212")
    
    def __str__(self):
        return "Theme Settings"




class BackgroundImage(models.Model):
    name = models.CharField(max_length=255)
    background_image_1 = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    background_image_1_opacity = models.FloatField(default=1.0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    background_image_2 = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    background_image_2_opacity = models.FloatField(default=1.0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    background_image_3 = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    background_image_3_opacity = models.FloatField(default=1.0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.name

