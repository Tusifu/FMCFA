from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Select, TextInput, Textarea

class Pharmacist(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone =  models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateTimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Pharmacist"

class PharmacistForm(forms.ModelForm):

    class Meta:
        model = Pharmacist
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter pharcist"}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your Address"}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your phone"}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your email"}),
            'dob': TextInput(attrs={'class': 'form-control', 'type':'date'}),
        }