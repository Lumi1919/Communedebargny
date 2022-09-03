from django.forms import ModelForm
from django.forms import ModelForm, TextInput, TextInput, EmailField
from django import forms
from .models import Demarche




class DemarcheForm(forms.ModelForm):
    class Meta:
        model = Demarche
        fields = ['nom', 'prenom', 'mail', 'tel', 'document', 'piece_identite', 'adresse']

        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}),
            'mail' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'document' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Document souhaité'}),
            'piece_identite' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': "Pièce d'identité"}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
        }
