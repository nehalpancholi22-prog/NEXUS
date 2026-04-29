from django.urls import path
from .views import home,edit_project,project_detail,contact_view,login_view,logout_view
from .views import delete_project


urlpatterns = [
    path('', home, name='home'),
    path('project/<int:id>/', project_detail, name='project_detail'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit-project/<int:id>/', edit_project, name='edit_project'),
    path('delete-project/<int:id>/', delete_project, name='delete_project'),
]