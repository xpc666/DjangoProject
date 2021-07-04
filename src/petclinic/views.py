from django.shortcuts import render, get_object_or_404
from petclinic import forms
from petclinic import models

from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'petclinic/home.html')

def findOwner(request):
    form = forms.FindOwnerForm()
    if request.method == "POST":
    	form = forms.FindOwnerForm(request.POST)
    	if form.is_valid():
            last_name = form.clean_last_name()
            if len(last_name) == 0:
                owners = models.Owners.objects.all()
            else:
                owners = models.Owners.objects.filter(last_name__exact=last_name)
            if owners.exists():
                # dict = {}
                # for owner in owners:
                #     dict[owner] = models.Pets.objects.filter(owner_id__exact=owner.id)
                return render(request, "petclinic/owners.html", {'owners' : owners}) #{'dict':dict})
            else:
                return render(request, "petclinic/find_owners.html", {'form': form, 'no_owners_found':'No owners with the given last name or there are no owners yet'})

    return render(request, "petclinic/find_owners.html", {"form":form})

def addOwner(request):
    form = forms.NewOwnerForm()

    if request.method == "POST":
    	form = forms.NewOwnerForm(request.POST)
    	if form.is_valid():
            owner = form.save()
            return render(request, "petclinic/owner_info.html", {'owner':owner})

    return render(request, "petclinic/add_owner.html", {'form':form})

def ownerDetail(request, pk):
    try:
        owner = models.Owners.objects.get(id=pk)
        # pets = models.Pets.objects.filter(owner_id=pk)
        # pet_visits = {};
        # for pet in pets:
        #     visits = models.Visits.objects.filter(pet_id=pet.id)
        #     pet_visits[pet] = visits

    except Owners.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'petclinic/owner_info.html', context={'owner': owner}) # , 'pets_visits': pet_visits

def editOwner(request, pk):
    obj= get_object_or_404(models.Owners, id=pk)
    form = forms.NewOwnerForm(request.POST or None, instance=obj)
    context= {'form': form}

    if request.method == "POST":
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request, "You successfully updated the owner")
            context= {'owner': obj}
            return render(request, 'petclinic/owner_info.html', context)
        else:
            context= {'owner': form, 'error': 'The form was not updated successfully. Please check content'}
    else:
        return render(request,'petclinic/edit_owner.html' , context)

def editPet(request, pk):
    obj= get_object_or_404(models.Pets, id=pk)
    form = forms.NewPetForm(request.POST or None, instance=obj)
    owner = models.Owners.objects.get(id=obj.owner_id)
    context= {'form': form, 'owner': owner}

    if request.method == "POST":
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request, "You successfully updated the pet")
            owner = models.Owners.objects.get(id=obj.owner_id)
            context= {'owner': owner}
            return render(request, 'petclinic/owner_info.html', context)
        else:
            context= {'form': form, 'error': 'The form was not updated successfully. Please check content'}
    else:
        return render(request,'petclinic/edit_pet.html' , context)

def addPet(request, pk):
    form = forms.NewPetForm()
    owner = models.Owners.objects.get(id=pk)
    if request.method == "POST":
    	form = forms.NewPetForm(request.POST)
    	if form.is_valid():
            pet = form.save(commit=False)
            pet.owner_id = pk
            pet.save()
            owner = models.Owners.objects.get(id=pk)
            return render(request, "petclinic/owner_info.html", {'owner':owner})

    return render(request, "petclinic/add_pet.html", {'form':form, 'owner':owner})

def addVisit(request, pk):
    pet = get_object_or_404(models.Pets, id=pk)
    form = forms.NewVisitForm()
    # owner = models.Owners.objects.get(id=obj.owner_id)
    context= {'form': form, 'pet': pet}

    if request.method == "POST":
        form = forms.NewVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.pet_id = pk
            visit.save()
            messages.success(request, "You successfully saved the pet visit")
            owner = models.Owners.objects.get(id=pet.owner_id)
            context= {'owner': owner}
            return render(request, 'petclinic/owner_info.html', context)
        else:
            context['error'] = 'The visit was not added successfully. Please check content'

    return render(request,'petclinic/add_visit.html' , context)

def vetsList(request):
    vets = models.Vets.objects.all()
    context = {'vets': vets}

    return render(request, 'petclinic/vets.html', context)
