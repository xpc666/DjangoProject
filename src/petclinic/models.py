# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.shortcuts import reverse

class Owners(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('owner_info', args=[str(self.id)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'owners'

class Pets(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    type = models.ForeignKey('Types', models.DO_NOTHING)
    owner = models.ForeignKey(Owners, models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'pets'

class Specialties(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'specialties'

class Types(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'types'

class VetSpecialties(models.Model):
    vet = models.ForeignKey('Vets', models.DO_NOTHING)
    specialty = models.ForeignKey(Specialties, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vet_specialties'
        unique_together = (('vet', 'specialty'),)


class Vets(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    specialties = models.ManyToManyField(Specialties, through='VetSpecialties')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'vets'

class Visits(models.Model):
    pet = models.ForeignKey(Pets, models.DO_NOTHING)
    visit_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visits'
