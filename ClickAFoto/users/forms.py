from django import forms
from .models import Login

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
        
    class Meta:
        model = Login
        fields = ('username','password','first_name','last_name','email','SQ1','SA1','SQ2','SA2','SQ3','SA3')
        