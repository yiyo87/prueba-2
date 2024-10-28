from django import forms
from equipoBasket.models import Equipo

class formularioEquipo (forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'