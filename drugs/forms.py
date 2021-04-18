from django import forms
from django.forms import ModelForm, TextInput, Select
from drugs.models import DrugsIssuing

class drugForm(forms.ModelForm):
    
    class Meta:
        model = DrugsIssuing
        fields = '__all__'
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder':'date'}),
        }


# class drugForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField()
#     address = forms.CharField(max_length=100)
#     dob = forms.DateTimeField()
#     province = forms.CharField(max_length=10)
#     district = forms.CharField(max_length=100)
#     sector = forms.CharField(max_length=100)
#     cell = forms.CharField(max_length=100)