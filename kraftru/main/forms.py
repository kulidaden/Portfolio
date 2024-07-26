from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError
from django import forms



def title_not_str(value):
    """
    Ця функція переверіє на коректність заповненого поля title
    """
    for i in str(value):
        if i in '0123456789!@#$%^&*()_+:;"\'':
            raise ValidationError({'title': "Ім'я та фамілія має містити тільки букви!"})
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        task = forms.ChoiceField(choices=Task.task_choice)
        fields = ["title", "number", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть ім'я та фамілію",
                'style': "width: 500px;font-size: 20px;height: 50px;"

            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер телефону',
                'style': "width: 500px; font-size: 20px;margin-top:10px; height: 50px;"
            }),
            "task": forms.Select(attrs={
                'class': 'form-control',

                'style': "width: 500px; font-size: 20px;margin-top:10px; height: 50px;"
            }),
        }
    def clean(self):
        super().clean()
        title_not_str(self.cleaned_data.get('title'))