from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Select, TextInput, Textarea

class HospitalAgent(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateTimeField()
    phone =  models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "HospitalAgent"


class HospitalAgentForm(forms.ModelForm):

    class Meta:
        model = HospitalAgent
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter hospital Agent"}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your Address"}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your phone"}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your email"}),
            'dob': TextInput(attrs={'class': 'form-control', 'type':'date'}),
        }