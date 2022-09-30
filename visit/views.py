from django.shortcuts import render
from tables.models import VisitModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VisitForm
from django.views.generic import UpdateView, CreateView

def visit_view(request):
    visit_objs = VisitModel.objects.all()
    return render(request, 'visit/visit_table.html', {'visit_objs': visit_objs})

def delete_visit(request, id):
    member = VisitModel.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('tables_visit'))


class VisitCreate(CreateView):
    form_class = VisitForm
    template_name = 'visit/create_visit.html'


class VisitUpdate(UpdateView):
    model = VisitModel
    template_name = 'visit/create_visit.html'
    form_class = VisitForm
# Create your views here.
