from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit_view, name="tables_visit"),
    path('create/', views.VisitCreate.as_view(), name='create_visit'),
    path('delete/<int:id>', views.delete_visit, name='visit-delete'),
    path('edit/<int:pk>', views.VisitUpdate.as_view(), name='visit-update'),
]
