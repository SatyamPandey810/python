from django import forms

class UsersForm(forms.Form):
    FirstName = forms.CharField()
    lastName = forms.CharField()
    


    