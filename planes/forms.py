from django import forms
from .models import Plan_Contratado

class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan_Contratado
        fields = {}