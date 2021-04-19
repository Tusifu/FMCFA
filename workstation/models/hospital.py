from django.db import models
from workers.models.hosAgent import HospitalAgent
from django import forms
from django.forms import ModelForm
from django.forms import Select, TextInput, Textarea


class Hospital(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    agent = models.ForeignKey(HospitalAgent, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    class Meta:
        db_table = "Hospital"



class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter pharcist"}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your Address"}),
            'agent': forms.Select(attrs={'class': 'h-form-control'}),

        }
    
