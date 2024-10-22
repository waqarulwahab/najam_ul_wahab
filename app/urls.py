from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('portfolio-details/<int:project_id>/', portfolio_details, name='portfolio-details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
