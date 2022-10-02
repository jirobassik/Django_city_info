from django.shortcuts import render
from tables.models import EventModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView, CreateView
from .forms import EventForm
from django.db.models import Q
from datetime import date, timedelta


def event_view(request):
    event_objs = EventModel.objects.all()
    today_date = date.today()
    week_end = today_date + timedelta(days=14)
    return render(request, 'event/event_table.html',
                  {'event_objs': event_objs, 'search': False, 'today': today_date, 'week_end': week_end, })


def delete_event(request, id):
    member = EventModel.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('tables_event'))


def search_event_date(request):
    if request.method == 'POST':
        today_date = date.today()
        week_end = today_date + timedelta(days=14)
        event_objs = EventModel.objects.filter(Q(date__gte=today_date,
                                                 date__lt=week_end)).select_related("id_object")
        return render(request, 'event/event_table.html',
                      {'event_objs': event_objs, 'search': True, 'today': today_date, 'week_end': week_end, })
    else:
        return HttpResponseRedirect(reverse('tables_event'))


class EventCreate(CreateView):
    form_class = EventForm
    template_name = 'event/create_event.html'


class EventUpdate(UpdateView):
    model = EventModel
    template_name = 'event/create_event.html'
    form_class = EventForm

# Create your views here.
