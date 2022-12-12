from django import forms
from .models import ObjectModel
from valid_func import valid_str


class ObjectForm(forms.ModelForm):
    class Meta:
        model = ObjectModel
        fields = ['name', 'type_o', 'address', 'num_seat', 'id_owner', 'season_date_open', 'season_date_close', ]

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название объекта'
            }),
            'type_o': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип объекта'
            }),
            'address': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс'
            }),
            'num_seat': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество мест'
            }),
            'id_owner': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Владелец'
            }),
            'season_date_open': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Сезонная дата открытия',
                'type': 'date'
            }),
            'season_date_close': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Сезонная дата закрытия',
                'type': 'date'
            }),
        }

    def clean(self):
        super(ObjectForm, self).clean()

        name = self.cleaned_data.get('name')
        type_o = self.cleaned_data.get('type_o')
        address = self.cleaned_data.get('address')
        season_date_open = self.cleaned_data.get('season_date_open')
        season_date_close = self.cleaned_data.get('season_date_close')

        dict_valid = {"name": name, "type_o": type_o, "address": address}

        for key, value in dict_valid.items():
            valid_str.check_for_numeric(self, key, value)

        if season_date_open is not None and season_date_close is not None \
                and season_date_close <= season_date_open:
            self._errors['season_date_open'] = self.error_class([
                'Дата открытия должна быть меньше даты закрытия'])

        if season_date_open is not None and season_date_close is None \
                or season_date_open is None and season_date_close is not None:
            self._errors['season_date_open'] = self.error_class([
                'Обе даты должны быть заполнены'])

        return self.cleaned_data

    # def clean_name(self):
    #     data_name = self.cleaned_data['name']
    #     if data_name.isnumeric():
    #         raise forms.ValidationError("Значение должно быть строкой")
    #     return data_name
    #
    # def clean_type_o(self):
    #     data_type_o = self.cleaned_data['type_o']
    #     if data_type_o.isnumeric():
    #         raise forms.ValidationError("Значение должно быть строкой")
    #     return data_type_o
    #
    # def clean_address(self):
    #     data_address = self.cleaned_data['address']
    #     if data_address .isnumeric():
    #         raise forms.ValidationError("Значение должно быть строкой")
    #     return data_address
