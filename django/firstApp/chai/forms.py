from django import forms
from .models import ChaiVaity

class ChaiVarityForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=ChaiVaity.objects.all(),label="select chai varity")