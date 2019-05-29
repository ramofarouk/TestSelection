from django.forms import ModelForm, TextInput
from .models import Communes


class CityForm(ModelForm):
    class Meta:
        model = Communes
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
