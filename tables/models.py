from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class OwnerModel(models.Model):
    face_view = models.CharField("Тип лица", max_length=20, null=False)
    name = models.CharField("Имя владельца", max_length=20, null=False)
    full_name_head = models.CharField("ФИО руководителя", max_length=100, null=False)
    contact_number = PhoneNumberField("Номер телефона", max_length=15, null=False, unique=True, region="BY")
    opening_date = models.DateField("День открытия", null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('tables_owner')


class ObjectModel(models.Model):
    name = models.CharField("Название объекта", max_length=30, null=False)
    type_o = models.CharField("Тип объекта", max_length=30, null=False)
    address = models.CharField("Адресс объекта", max_length=50, null=False)
    num_seat = models.PositiveIntegerField("Количество мест", null=False, default=0)
    id_owner = models.ForeignKey(OwnerModel, on_delete=models.SET_NULL, verbose_name='Владелец', null=True)
    season_date_open = models.DateField("Сезонный день открытия", null=True, blank=True)
    season_date_close = models.DateField("Сезонный день закрытия", null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('tables')


class VisitModel(models.Model):
    id_object = models.ForeignKey(ObjectModel, on_delete=models.CASCADE, verbose_name="Название объкта", null=False)
    date = models.DateField("Дата учета", null=False)
    num_visit = models.PositiveIntegerField("Количество посетивших", null=False, default=0)

    def __str__(self):
        return str(self.id_object)

    @staticmethod
    def get_absolute_url():
        return reverse('tables_visit')


class EventModel(models.Model):
    id_object = models.ForeignKey(ObjectModel, on_delete=models.CASCADE, verbose_name="Название объкта", null=False)
    name = models.CharField("Название мероприятия", max_length=50, null=False)
    kind = models.CharField("Тип мероприятия", max_length=50, null=False)
    date = models.DateField("День мероприятия", null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('tables_event')

# Create your models here.
