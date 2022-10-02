from django import forms
from tables.models import VisitModel, ObjectModel
from django.db.models import Q

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

    def clean(self):
        super(VisitForm, self).clean()

        id_object = self.cleaned_data.get('id_object')
        date = self.cleaned_data.get('date')

        date_open = ObjectModel.objects.get(Q(name__contains=id_object)).season_date_open
        date_close = ObjectModel.objects.get(Q(name__contains=id_object)).season_date_close

        if not ObjectModel.objects.filter(Q(name__contains=id_object) &
                                          Q(season_date_close__gte=date, season_date_open__lte=date)
                                          | Q(name__contains=id_object) &
                                          Q(season_date_close__exact=None, season_date_open__exact=None)):
            self._errors['date'] = self.error_class([
                f'Дата должна быть между промежутком {date_open} и {date_close}'])

        return self.cleaned_data
