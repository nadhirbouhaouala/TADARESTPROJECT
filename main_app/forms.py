from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['comment'].widget.attrs = {
            'class': 'form-control'#col-md-6
        }

    class Meta:
        model = Task
        fields = ('file','comment',)