from django import forms
from register.models import user

class NewUser(forms.ModelForm):
    class Meta:
        model= user
        fields= '__all__'
