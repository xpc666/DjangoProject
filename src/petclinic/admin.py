from django.contrib import admin
from petclinic.models import Owners, Pets, Specialties, Types, VetSpecialties, Vets, Visits

# Register your models here.
admin.site.register(Owners)
admin.site.register(Pets)
admin.site.register(Specialties)
admin.site.register(Types)
admin.site.register(VetSpecialties)
admin.site.register(Vets)
admin.site.register(Visits)
