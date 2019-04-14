from . import views
from django.urls import path

urlpatterns = [
    # Paths for the restaurant menu API

    # view.menu_sections deals with all operations relating to menu sections as a whole.
    # This includes getting all menu sections and adding a new section to the menu.
    path('menusection/', views.menu_sections, name='Menu Sections'),

    # view.specific_menu_section deals with all operations relating to a specific menu section.
    # This includes retrieving the specific menu section, editing, and deleting it.
    path('menusection/<int:id>/', views.specific_menu_section, name='Menu Section'),
]