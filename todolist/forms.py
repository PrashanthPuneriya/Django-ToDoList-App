from django import forms
from .models import ToDo
class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'due_date']
        widgets = {'due_date' : forms.DateInput(attrs={'type':'date'})}
        # widgets = {'due_date' : forms.SelectDateWidget}
        

class ToDoSearchForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name']