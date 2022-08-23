from django.forms import ModelForm

from lista.models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        exclude = ['created_at', 'updated_at']