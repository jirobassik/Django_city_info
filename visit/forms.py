from django import forms
from tables.models import VisitModel


class VisitForm(forms.ModelForm):
    class Meta:
        model = VisitModel
        fields = ['id_object', 'date', 'num_visit', ]

        widgets = {
            "id_object": forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Объект'
            }),
            'date': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Дата мероприятия',
                'type': 'date'
            }),
            'num_visit': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество посетивших'
            }),
        }
