from django import forms
from tables.models import OwnerModel
from valid_func import valid_str

class OwnerForm(forms.ModelForm):
    class Meta:
        model = OwnerModel
        fields = ['face_view', 'name', 'full_name_head', 'contact_number', 'opening_date', ]

        widgets = {
            "face_view": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип лица'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя владельца'
            }),
            'full_name_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО руководителя'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'opening_date': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Дата открытия',
                'type': 'date'
            }),
        }

    def clean(self):
        super(OwnerForm, self).clean()

        face_view = self.cleaned_data.get('face_view')
        name = self.cleaned_data.get('name')
        full_name_head = self.cleaned_data.get('full_name_head')

        dict_valid = {"face_view": face_view, "name": name, "full_name_head": full_name_head}

        for key, value in dict_valid.items():
            valid_str.check_for_numeric(self, key, value)

        return self.cleaned_data
