from .models import Service
from django.forms import ModelForm, TextInput, NumberInput,Textarea

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name','description', 'price','duration','lesson_duration']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Название услуги/тарифа'
            }),
            "description": Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Описание услуги/тарифа'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Цена услуги/тарифа за занятие(в рублях)'
            }),
            "duration": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Длительность услуги/тарифа(в днях)'
            }),
            "lesson_duration": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Длительность занятия(в минутах)'
            })
        }