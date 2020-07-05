from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HiddenUserCreationForm(UserCreationForm):
    # Overriding first_name field
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Defining our own label for password2 field
        self.fields['password2'].label = 'Confirm Password'