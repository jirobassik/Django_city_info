from django.shortcuts import render
from .models import ObjectModel
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView
from django.urls import reverse
from .forms import ObjectForm
from django.db.models import Q


def object_view(request):
    main_objs = ObjectModel.objects.all()
    type_obj = ObjectModel.objects.all().only("type_o")
    return render(request, 'object/object_table.html', {'main_objs': main_objs, 'search': False, 'type_obj': type_obj})


def delete_object(request, id):
    member = ObjectModel.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('tables'))


def search(request):
    type_object_filter = ObjectModel.objects.all().only("type_o")
    if request.method == 'POST':
        searched = request.POST['q']
        type_obj = request.POST['type_ob']

        if searched != "" and type_obj == "":
            # main_objs = ObjectModel.objects.filter(Q(season_date_close__gte=searched,
            #                                          season_date_open__lte=searched) | Q(season_date_close__exact=None))
            main_objs = ObjectModel.objects.raw(
                'select * from tables_objectmodel where %s between season_date_open and '
                'season_date_close or season_date_close is null', [searched])
            # season_date_close__exact ищет именно день месяц год
            return render(request, 'object/object_table.html',
                          {'main_objs': main_objs, 'search': True, 'type_obj': type_object_filter})

        elif searched == "" and type_obj != "":
            # main_objs = ObjectModel.objects.filter(Q(type_o__contains=type_obj))
            main_objs = ObjectModel.objects.raw('select * from tables_objectmodel where type_o = %s', [type_obj])
            return render(request, 'object/object_table.html',
                          {'main_objs': main_objs, 'search': True, 'type_obj': type_object_filter})

        elif searched != "" and type_obj != "":
            # main_objs = ObjectModel.objects.filter(Q(type_o__contains=type_obj) &
            #                                        Q(season_date_close__gte=searched,
            #                                          season_date_open__lte=searched) | Q(type_o__contains=type_obj) & Q(
            #     season_date_close__exact=None))
            main_objs = ObjectModel.objects.raw('select * from tables_objectmodel where type_o = %s and %s '
                                                'between season_date_open and season_date_close '
                                                'or type_o = %s and season_date_close is null',
                                                [type_obj, searched, type_obj])
            return render(request, 'object/object_table.html',
                          {'main_objs': main_objs, 'search': True, 'type_obj': type_object_filter})
        else:
            return HttpResponseRedirect(reverse('tables'))


class ObjectCreate(CreateView):
    form_class = ObjectForm
    template_name = 'object/create_object.html'


class ObjectUpdate(UpdateView):
    model = ObjectModel
    template_name = 'object/create_object.html'
    form_class = ObjectForm
