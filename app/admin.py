from django import forms
from django.utils.html import mark_safe
from django.contrib import admin
from django.utils.html import format_html
from .models import Client
from django.utils import timezone
from django.forms.widgets import SelectDateWidget
from .models import AboutMe
from .models import Project,  ProjectCategory, ProjectImage
from .models import ThemeSettings
from .models import AchievementsSection
from .models import Experience
from .models import Service
from .models import BackgroundImage
from .models import Skill

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'
        widgets = {
            'birthday': SelectDateWidget(years=range(1900, timezone.now().year + 1))
        }

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    form = AboutMeForm
    list_display = ('name', 'title', 'email', 'phone', 'city')



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_tag')

    def logo_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.logo.url))
        return '-'
    
    logo_tag.short_description = 'Logo'




@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)







class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty image fields to display initially



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'project_date', 'image_tag')
    inlines = [ProjectImageInline]
    list_per_page = 10  # This will display 20 rows per pag
    def image_tag(self, obj):
        if obj.images.exists():
            # Display the first image related to the project
            first_image = obj.images.first()
            return mark_safe(f'<img src="{first_image.image.url}" width="100" height="100" />')
        return "No Image"

    image_tag.short_description = 'Image'

admin.site.register(Project, ProjectAdmin)




@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_year', 'end_year')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')





admin.site.register(AchievementsSection)

admin.site.register(ThemeSettings)



class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'image_tag')  # Display image in list view
    readonly_fields = ('image_tag',)  # Display image in the detail view

admin.site.register(Skill, SkillAdmin)







@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'background_image_1_tag', 'background_image_2_tag', 'background_image_3_tag')

    def background_image_1_tag(self, obj):
        if obj.background_image_1:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.background_image_1.url))
        return '-'

    def background_image_2_tag(self, obj):
        if obj.background_image_2:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.background_image_2.url))
        return '-'

    def background_image_3_tag(self, obj):
        if obj.background_image_3:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.background_image_3.url))
        return '-'

    background_image_1_tag.short_description = 'Background Image 1'
    background_image_2_tag.short_description = 'Background Image 2'
    background_image_3_tag.short_description = 'Background Image 3'








