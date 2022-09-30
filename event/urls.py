from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_view, name="tables_event"),
    path('search/', views.search_event_date, name='search_event'),
    path('create/', views.EventCreate.as_view(), name='create_event'),
    path('delete/<int:id>', views.delete_event, name='event-delete'),
    path('edit/<int:pk>', views.EventUpdate.as_view(), name='event-update'),
]
