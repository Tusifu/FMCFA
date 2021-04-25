from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Select, TextInput, Textarea
# Create your models here.
class Beneficiary(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateTimeField()
    province = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    cell = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "Beneficiary"

class BeneficiaryForm(forms.ModelForm):

    class Meta:
        model = Beneficiary
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter beneficiary"}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your Address"}),
            'age': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your age"}),
            'province': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your province"}),
            'dob': TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'district': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your district"}),
            'sector': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your sector"}),
            'cell': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your cell"}),
            
        }
