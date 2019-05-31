from django.forms import ModelForm, TextInput, forms
from .models import Communes, Users


class CityForm(ModelForm):
    class Meta:
        model = Communes
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
