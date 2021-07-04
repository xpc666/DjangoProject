from django.urls import path
from petclinic import views

# app_name = 'petclinic'

urlpatterns = [
    path('', views.home, name='home'),
    path('find_owner', views.findOwner, name='find_owner'),
    path('add_owner', views.addOwner, name='add_owner'),
    path('owners/<int:pk>', views.ownerDetail, name='owner_info'),
    path('edit_owner/<int:pk>', views.editOwner, name='edit_owner'),
    path('edit_pet/<int:pk>', views.editPet, name='edit_pet'),
    path('add_visit/<int:pk>', views.addVisit, name='add_visit'),
    path('add_pet/<int:pk>', views.addPet, name='add_pet'),
    path('vets_list', views.vetsList, name='vets_list'),
]
