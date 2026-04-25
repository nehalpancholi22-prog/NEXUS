from django.urls import path
from .views import home, project_detail,contact_view

urlpatterns = [
    path('', home, name='home'),
    path('project/<int:id>/', project_detail, name='project_detail'),
    path('contact/', contact_view, name='contact'),
]