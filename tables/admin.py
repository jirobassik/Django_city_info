from django.contrib import admin
from .models import OwnerModel, ObjectModel, EventModel, VisitModel

admin.site.register(OwnerModel)
admin.site.register(ObjectModel)
admin.site.register(EventModel)
admin.site.register(VisitModel)

# Register your models here.
