from django import forms
from tables.models import EventModel, ObjectModel
from valid_func import valid_str
from django.db.models import Q


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

        id_object = self.cleaned_data.get('id_object')
        name = self.cleaned_data.get('name')
        kind = self.cleaned_data.get('kind')
        date = self.cleaned_data.get('date')

        date_open = ObjectModel.objects.get(Q(name__contains=id_object)).season_date_open
        date_close = ObjectModel.objects.get(Q(name__contains=id_object)).season_date_close

        if not ObjectModel.objects.filter(Q(name__contains=id_object) &
                                          Q(season_date_close__gte=date, season_date_open__lte=date)
                                          | Q(name__contains=id_object) &
                                          Q(season_date_close__exact=None, season_date_open__exact=None)):
            self._errors['date'] = self.error_class([
                f'Дата должна быть между промежутком {date_open} и {date_close}'])

        dict_valid = {"name": name, "kind": kind, }

        for key, value in dict_valid.items():
            valid_str.check_for_numeric(self, key, value)

        return self.cleaned_data
