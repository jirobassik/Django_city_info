from django import forms
from tables.models import EventModel
from valid_func import valid_str

class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['id_object', 'name', 'kind', 'date']

        widgets = {
            "id_object": forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Объект'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название мероприятия'
            }),
            'kind': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип'
            }),
            'date': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={
                'class': 'form-control',
                'placeholder': 'Дата мероприятия',
                'type': 'date'
            }),
        }

    def clean(self):
        super(EventForm, self).clean()

        name = self.cleaned_data.get('name')
        kind = self.cleaned_data.get('kind')

        # date = self.cleaned_data.get('address') Добавить валидацию, что дата, должна быть больше чем дата создания
        # объкта и нельзя выставлять на промежуток закрытия

        dict_valid = {"name": name, "kind": kind, }

        for key, value in dict_valid.items():
            valid_str.check_for_numeric(self, key, value)

        return self.cleaned_data
