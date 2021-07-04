from django import forms
from django.forms import ValidationError
from petclinic import models
import re

class FindOwnerForm(forms.Form):
    last_name = forms.CharField(
            required=False,
            max_length=30,
            label='',
            error_messages = {'max_length': 'The maximum length for a last name should be less than 30 characters'})

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        pattern = r'[^\.a-zA-Z]'
        search=re.compile(r'[^a-zA-Z]').search
        if(bool(search(data))):
            raise ValidationError('Last name should contain only characters')

        return data

class NewOwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owners
        fields = '__all__'

class NewPetForm(forms.ModelForm):
    class Meta:
        model = models.Pets
        fields = ('name', 'birth_date', 'type')

class NewVisitForm(forms.ModelForm):
    class Meta:
        model = models.Visits
        fields = ('visit_date', 'description')
