from django.shortcuts import render
from tables.models import OwnerModel
from .forms import OwnerForm
from django.views.generic import UpdateView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse

def owner_view(request):
    owner_objs = OwnerModel.objects.all()
    return render(request, 'owner/owner_table.html', {'owner_objs': owner_objs})

def delete_owner(request, id):
    member = OwnerModel.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('tables_owner'))


class OwnerCreate(CreateView):
    form_class = OwnerForm
    template_name = 'owner/create_owner.html'


class OwnerUpdate(UpdateView):
    model = OwnerModel
    template_name = 'owner/create_owner.html'
    form_class = OwnerForm

# Create your views here.
